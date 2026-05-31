import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getFirestore, collection, getDocs, addDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";

// Firebase configuration using automatic config from hosting or fallback
const firebaseConfig = {
  projectId: "houset-luxembourg-official",
  // In a real scenario we need the web API key here, but we will fall back to local storage if Firestore fails
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const WHATSAPP_NUMBER = "5491170655165";

// --- Cart Logic ---
class Cart {
    constructor() {
        this.items = JSON.parse(localStorage.getItem('cart') || '[]');
        this.updateBadge();
        this.renderCartIfPresent();
    }

    add(product) {
        const existing = this.items.find(i => i.id === product.id);
        if (existing) {
            existing.qty += 1;
        } else {
            this.items.push({ ...product, qty: 1 });
        }
        this.save();
        this.showToast("Producto agregado al carrito");
    }

    remove(id) {
        this.items = this.items.filter(i => i.id !== id);
        this.save();
        this.renderCartIfPresent();
    }

    updateQty(id, delta) {
        const item = this.items.find(i => i.id === id);
        if (item) {
            item.qty += delta;
            if (item.qty <= 0) this.remove(id);
            else {
                this.save();
                this.renderCartIfPresent();
            }
        }
    }

    save() {
        localStorage.setItem('cart', JSON.stringify(this.items));
        this.updateBadge();
    }

    getTotal() {
        return this.items.reduce((sum, item) => sum + (item.price * item.qty), 0);
    }

    updateBadge() {
        const totalItems = this.items.reduce((sum, item) => sum + item.qty, 0);
        document.querySelectorAll('.shopping-cart-badge').forEach(el => {
            el.innerText = totalItems;
            el.style.display = totalItems > 0 ? 'flex' : 'none';
        });
    }

    renderCartIfPresent() {
        const cartContainer = document.getElementById('cart-items-container');
        if (!cartContainer) return;
        
        cartContainer.innerHTML = '';
        if (this.items.length === 0) {
            cartContainer.innerHTML = '<p class="p-6 text-on-surface-variant text-center">Tu carrito está vacío.</p>';
            document.getElementById('cart-subtotal').innerText = '$0';
            document.getElementById('cart-total').innerText = '$0';
            return;
        }

        this.items.forEach(item => {
            const html = `
            <div class="flex flex-col sm:flex-row gap-6 p-6 border border-outline-variant bg-surface relative group">
                <button onclick="window.cart.remove('${item.id}')" aria-label="Eliminar" class="absolute top-4 right-4 text-outline hover:text-error transition-colors">
                    <span class="material-symbols-outlined">close</span>
                </button>
                <div class="w-full sm:w-32 h-40 sm:h-auto flex-shrink-0 bg-surface-container-low border border-outline-variant relative overflow-hidden">
                    <img src="${item.image}" alt="${item.name}" class="absolute inset-0 w-full h-full object-cover">
                </div>
                <div class="flex flex-col justify-between flex-grow">
                    <div>
                        <h3 class="text-headline-md font-headline-md text-on-background mb-1">${item.name}</h3>
                        <p class="text-body-md font-body-md text-on-surface-variant mb-4">${item.desc || ''}</p>
                    </div>
                    <div class="flex justify-between items-center mt-auto">
                        <div class="flex items-center border border-outline-variant rounded bg-surface-container-lowest">
                            <button class="px-3 py-1 text-on-surface-variant hover:text-primary" onclick="window.cart.updateQty('${item.id}', -1)">-</button>
                            <input class="w-10 text-center bg-transparent border-none text-body-md font-body-md p-0 focus:ring-0" type="number" value="${item.qty}" readonly/>
                            <button class="px-3 py-1 text-on-surface-variant hover:text-primary" onclick="window.cart.updateQty('${item.id}', 1)">+</button>
                        </div>
                        <span class="text-body-lg font-body-lg text-primary">$${item.price.toLocaleString('es-AR')}</span>
                    </div>
                </div>
            </div>`;
            cartContainer.insertAdjacentHTML('beforeend', html);
        });

        const totalStr = '$' + this.getTotal().toLocaleString('es-AR');
        document.getElementById('cart-subtotal').innerText = totalStr;
        document.getElementById('cart-total').innerText = totalStr;
    }

    checkout() {
        if (this.items.length === 0) {
            alert("Tu carrito está vacío.");
            return;
        }
        let text = "Hola! Quisiera realizar el siguiente pedido:%0A%0A";
        this.items.forEach(item => {
            text += `- ${item.qty}x ${item.name} ($${(item.price * item.qty).toLocaleString('es-AR')})%0A`;
        });
        const giftMsg = document.getElementById('gift-message')?.value;
        if (giftMsg) {
            text += `%0A🎁 Mensaje de regalo:%0A"${giftMsg}"%0A`;
        }
        text += `%0A*Total estimado: $${this.getTotal().toLocaleString('es-AR')}*%0A`;
        text += `%0APor favor, indícame los pasos para abonar y cómo puedo personalizar mi pedido.%0A`;
        
        window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${text}`, '_blank');
        this.items = [];
        this.save();
        this.renderCartIfPresent();
    }

    showToast(msg) {
        const toast = document.createElement('div');
        toast.className = 'fixed bottom-20 left-1/2 transform -translate-x-1/2 bg-surface-container-highest border border-primary text-primary px-6 py-3 rounded-full shadow-lg z-50 text-label-md transition-opacity duration-300 opacity-0';
        toast.innerText = msg;
        document.body.appendChild(toast);
        setTimeout(() => toast.classList.remove('opacity-0'), 10);
        setTimeout(() => {
            toast.classList.add('opacity-0');
            setTimeout(() => toast.remove(), 300);
        }, 2500);
    }
}

// Add global cart instance
window.cart = new Cart();

// Wait for DOM to wire up buttons
document.addEventListener('DOMContentLoaded', () => {
    // Inject floating WhatsApp button
    const waBtn = document.createElement('a');
    waBtn.href = `https://wa.me/${WHATSAPP_NUMBER}?text=Hola!%20Quisiera%20hacer%20una%20consulta%20sobre%20los%20productos%20y%20c%C3%B3mo%20personalizarlos.`;
    waBtn.target = "_blank";
    waBtn.className = "fixed bottom-6 right-6 w-14 h-14 bg-[#25D366] text-white rounded-full flex items-center justify-center shadow-lg hover:scale-110 transition-transform z-[9999]";
    waBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="currentColor" viewBox="0 0 16 16"><path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c-.003 1.396.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/></svg>';
    document.body.appendChild(waBtn);

    // Make shopping bags open the cart page
    document.querySelectorAll('button[aria-label="Carrito"], button[aria-label="Carrito de compras"]').forEach(btn => {
        btn.onclick = () => window.location.href = 'carrito.html';
    });

    // Make header logo open index
    document.querySelectorAll('h1').forEach(h1 => {
        if(h1.innerText.includes('Juan & Beltrán')) {
            h1.style.cursor = 'pointer';
            h1.onclick = () => window.location.href = 'index.html';
        }
    });
});
