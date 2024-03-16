<template>
    <div class="wrapper">
        <div class="options-wrapper">
            <router-link to = "/" class = "nav-part home">HOME</router-link>
            <router-link to = "/buy" class = "nav-part buy">BUY</router-link>
            <router-link to = "/sell" class = "nav-part sell">SELL</router-link>
            <router-link to = "/wishlist" class = "nav-part wishlist">WISHLIST</router-link>
        </div>
    </div>
</template>

<script>
export default{
    name: "pageNav",
}
</script>

<style scoped>
.wrapper{
    width: 100%;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
}

.options-wrapper{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 1rem;
    gap: 0.8rem;
    margin-right: auto;
    margin-left: auto;
}
.nav-part{
    display: inline-block;
    letter-spacing: 0.2rem;
    margin-bottom: 0.1rem;
    border-radius: 0.3rem;
    padding: 0.5rem 1rem;
    font-size: 1.2rem;
    text-decoration: none;
    color: #28d4ec
}
.nav-part:hover{
    margin-bottom: 0;
    border-bottom: 0.1rem solid white;
}

.router-link-active{
    background-color: #28d4ec;
    color: black;
}

.router-link-active:hover{
    border-bottom: none;
}
</style>