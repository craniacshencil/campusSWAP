<template>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
<div class = "back-overlay">
    <div class="top-row">
        <h1 class = branding>CampusSwap</h1>
        <InputGroup>
            <Button label="Search" />
            <InputText placeholder="Keyword" />
        </InputGroup>
        <div class = options>
            <Button @click = "gotoLogin" label = "Login" />
            <Button @click = "gotoRegister" label = "Register" />
        </div>
        
        
    </div>
    <div class="wrapper">
    <div class="options-wrapper">
            <Button @click = 'this.$router.push("/")' text class = "nav-part home">HOME</Button>
            <Button @click = 'this.$router.push("/buy")' text class = "nav-part buy">BUY</Button>
            <Button @click = 'this.$router.push("/sell")' text class = "nav-part sell">SELL</Button>
            <Button @click = 'this.$router.push("/wishlist")' text class = "nav-part wishlist">CONTACT US</Button>
        </div>
    </div>
     
    <div class="category-section">
        <h2 class="the-text">Swap Your Gear Here</h2>
        <div class="categories">
          <div class="category"><img src="@/assets/engineering.jpeg" alt="electronics-logo"><span class="cat-text">Electronics</span></div>
          <div class="category"><img src="@/assets/books.jpeg" alt="book-logo"><span class="cat-text">Books</span></div>
          <div class="category"><img src="@/assets/notes.jpeg" alt="notes-logo"><span class="cat-text">Notes</span></div>
          <div class="category"><img src="@/assets/color.jpeg" alt=""><span class="cat-text">Category 4</span></div>
          <div class="category"><img src="@/assets/color.jpeg" alt=""><span class="cat-text">Category 5</span></div>
        </div>
      </div>
      <div class="main-body">
        <h2 style="color: rgb(255, 255, 255); padding: 0  0 10px 10px;" >Recomended for you</h2>
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
    import Button from 'primevue/button'
    export default{
        components:{ Button, InputText, InputGroup },
        data(){
            return{

            }
        },

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
    .wrapper{
        width: 100%;
        padding: 0 20px;
        display: flex;
        justify-content: space-around;
        
    }
    .options-wrapper{
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin: 1rem;
        background-color: #172554;
    }
    .back-overlay{
        background-color: #172554;
        border-radius: 10px;
        border: 20px solid #22d3ee;
        width: 100%;
        height: 100%;
    }

    .top-row{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 0 20px;
    }
    h1.branding{
        display: inline-block; 
        color: white;
        font-size: 78px;
        font-family: "Cormorant Garamond";
        padding: 0;
        margin: 0px 60px 0px 0px;
    }

    .nav-part{
    letter-spacing: 0.2rem;
    margin-bottom: 0.1rem;
    background-color: #000000;
}
.nav-part:hover{
    margin-bottom: 0;
    border-bottom: 0.1rem solid white;
}

    Button{
        margin: 3px;
    }
    .logo img {
    max-width: 100px; 
    height: auto;
    margin-right: 60px;
    margin-left: 20px;
}


.search-bar {
    flex: 3; 
    display: flex;
    align-items: center;
    padding: 0 40px 0;
    
    
}

.search-bar input[type="text"] {
    width: 100%; 
    padding: 8px;
    border: 2px solid black;
    border-radius: 25px; 
    background-color: #ffffff; 
    /* outline: none; */
}

.search-bar button {
    background-color: #2980af; 
    border: none;
    padding: 5px;
    border-radius: 25px; 
    cursor: pointer;   
}

.search-bar button svg {
    width: 20px; 
    height: 20px;
    fill: #ffffff; 
}

.user-actions {
    flex: 1; 
    display: flex;
    align-items: center;
}

.user-actions a {
    margin-left: 50px; 
}


.search-container {
    position: relative;
}
  
.search-container input[type="text"] {
    width: 200px; 
    padding-right: 40px; 
}
  
.search-container button {
    position: absolute;
    top: 0;
    right: 0;
    width: 40px; 
    height: 100%;
}
  

.options-container {
    background-color: rgba(255, 255, 255, 0.735); 
    text-align: center;
}
  
.options {
    display: flex;
    justify-content: space-around;
    padding: 10px 100px;
}
  
.option {
    padding: 10px 20px;
    cursor: pointer;
    transition:  0.3s ease;
    background-color: #22d3ee;
    border-radius: 20px;
}
  
.option:hover {
    background-color: rgb(181, 180, 180);
    color: white;
}
  
.category-section {
    background-color: #0e1d2f;
    color: white;
    padding: 0 20px;
    text-align: center;
    height: 175px;
}
  
.categories {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 20px;
}
  
.category {
    /* padding: 10px 20px;
    margin: 10px;
    
    background-color: rgba(255, 255, 255, 0.2); 
    */ 
    transition: transform 0.3s ease, border-bottom 0.3s ease;
    width: 150px; 
    height: 150px; 
    border-radius: 50%; 
    overflow: hidden; 
    position: relative; 
    margin: 20px;
}
  
.category:hover {
    transform: scale(1.1); 
    cursor: pointer;
}

.the-text{
    padding: 20px;
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
    color: black;
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
    border: 1px solid #ddd;
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
    margin: 2px 0;
    padding: 5px;
}
  
.listing p.description {
    flex-grow: 1;
    margin-bottom: 10px;
    padding: 5px;

    
}
  
.listing button {
    margin-top: auto;

    padding: 10px 0px;
    background-color: #2980af;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
    transition: background-color 0.3s;
}
  
.listing button:hover {
    background-color: #ff7a37;
}
  

.listing:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
  
</style>
