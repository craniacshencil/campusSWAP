<template>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
<div class = "back-overlay">
    <pageHeader />
    <pageNav /> 
    <div class="category-section">
        <h2 class="the-text">SWAP YOUR GEAR HERE</h2>
        <div class="categories">
          <div class="category"><img src="@/assets/engineering.jpeg" alt="electronics-logo"><span class="cat-text">Electronics</span></div>
          <div class="category"><img src="@/assets/books.jpeg" alt="book-logo"><span class="cat-text">Books</span></div>
          <div class="category"><img src="@/assets/notes.jpeg" alt="notes-logo"><span class="cat-text">Notes</span></div>
          <div class="category"><img src="@/assets/tools.jpg" alt=""><span class="cat-text">Tools</span></div>
          <div class="category"><img src="@/assets/printer.jpg" alt=""><span class="cat-text">Printers</span></div>
        </div>
      </div>
      <div class="main-body">
        <h2 style="font-size: 2rem; color: rgb(255, 255, 255); padding: 0  0 10px 10px;" >Recomended for you</h2>
        <div class="listings-section">
          <div class="listing">
            <img src="@/assets/books.jpeg" alt="Item 1">
            <h3>Java Study Material</h3>
            <p class="description">
                Java resources to help you along your journey.</p>
            <button>Contact Seller</button>
          </div>
          
          <div class="listing">
            <img src="@/assets/notes.jpeg" alt="Item 2">
            <h3>EM - III Practice Problems</h3>
            <p class="description">Solving problems is crucial for mastering math concepts.
            </p>
            <button>Contact Seller</button>
          </div>
          
          <div class="listing">
            <img src="@/assets/campusswap_logo.jpeg" alt="Item 3">
            <h3>Buy Entire Website</h3>
            <p class="description">Establish a strong online presence for your brand or business.</p>
            <button>Contact Seller</button>
          </div>
          
          <div class="listing">
            <img src="@/assets/engineering.jpeg" alt="Item 4">
            <h3>Arduino Starter Kit</h3>
            <p class="description">
            Arduino kits are fantastic for learning about electronics.</p>
            <button>Contact Seller</button>
          </div>
          
          <div class="listing">
            <img src="@/assets/placeholder.webp" alt="Item 5">
            <h3>Item 5</h3>
            <p class="description">Description of Item 5</p>
            <button>Contact Seller</button>
          </div>
          
          <div class="listing">
            <img src="@/assets/placeholder.webp" alt="Item 6">
            <h3>Item 6</h3>
            <p class="description">Description of Item 6</p>
            <button>Contact Seller</button>
          </div>
        </div>
      </div>
</div>
</template>
<script>
    import InputGroup from 'primevue/inputgroup';
    import InputText from 'primevue/inputtext';
    import pageNav from '@/custom_comps/pageNav.vue';
    import pageHeader from '@/custom_comps/pageHeader.vue';
    export default{
        components:{ pageNav, pageHeader, InputText, InputGroup },
        methods: {
            gotoLogin(){
                this.$router.push("/login")
            },

            gotoRegister() {
                this.$router.push('/register')
            }
        }
    }
</script>

<style scoped>
.back-overlay{
    background-color: #090909;
    border-radius: 10px;
    width: 100%;
    height: 100%;
}
  
.category-section {
    background-color: #22d3ee;
    color: white;
    padding: 0 20px;
    text-align: center;
    height: 250px;
}
  
.categories {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin: 20px 0;
}
  
.category {
    /* padding: 10px 20px;
    margin: 10px;
    
    background-color: rgba(255, 255, 255, 0.2); 
    */ 
    transition: transform 0.3s ease, border-bottom 0.3s ease;
    width: 220px; 
    height: 220px; 
    border-radius: 50%; 
    overflow: hidden; 
    position: relative; 
    margin: 0 20px;
}
  
.category:hover {
    transform: scale(1.1); 
    cursor: pointer;
}

.the-text{
    color: black;
    font-size: 4rem;
    margin-bottom: 0;
    text-transform: capitalize;
    font-weight: 700;
    letter-spacing: 0.2rem;
}

.category img{
    width: 100%; 
    height: 100%; 
    object-fit: cover;    
}

.category span{
    position: absolute; 
    bottom: 0; 
    left: 0; 
    width: 100%; 
    padding: 10px 0; 
    color: #ccc;
    font-weight: bold;
    transition: background-color 0.3s  
}

.cat-text:hover{
    background-color: rgba(0, 0, 0, 0.5); 
    color: white;
}

.cat-text{
    color: white;
}

.main-body {
    padding: 200px 20px 20px;
}
  
.listings-section {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 50px;
}
  
.listing {
    display: flex;
    flex-direction: column;
    border: 2px solid #ddd;
    height: 370px;
    border-radius: 5px;
    overflow: hidden; 
    transition: transform 0.3s; 
    position: relative;
    /* width: 250px;
    height: 300px; */
}
  
.listing img {
    width: 100%;
    height: 200px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}
  
.listing h3 {
    margin: 0;
    padding: 0;
    margin-top: 0.5rem;
    padding-left: 0.3rem;
}
  
.listing p.description {
    flex-grow: 1;
    margin: 0;
    padding: 0;
    margin-top: 0.5rem;
    padding-left: 0.3rem;
}
  
.listing button {
    margin-top: auto;
    padding: 10px 0px;
    background-color: #2980af;
    color: white;
    font-weight: 700;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    transition: background-color 0.3s;
}
  
.listing button:hover {
    background-color: #ff7a37;
}
  

.listing:hover {
    transform: translateY(-2rem);
    box-shadow: 1px 1px 10px rgba(255, 255, 255, 0.5);
}
</style>
