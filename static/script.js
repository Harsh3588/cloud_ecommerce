document.addEventListener('DOMContentLoaded', function() {
    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');
    const cartCount = document.getElementById('cartCount');
    
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-check me-1"></i>Added!';
            this.classList.add('btn-added', 'disabled');
            
            const currentCount = parseInt(cartCount.textContent);
            cartCount.textContent = currentCount + 1;
            cartCount.parentElement.classList.add('cart-updated');
            
            fetch(this.href, { 
                method: 'GET',
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            })
            .then(response => response.json())
            .then(data => {
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.classList.remove('btn-added', 'disabled');
                    cartCount.parentElement.classList.remove('cart-updated');
                }, 1500);
            })
            .catch(error => {
                console.log('Cart update error:', error);
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.classList.remove('btn-added', 'disabled');
                }, 1500);
            });
        });
    });
});
