<template>
    <div class="wrapper">
        <div v-if = "this.$route.name === 'Buy'" class="filter-block card flex justify-content-center align-items-center">
            <Filters />
        </div>

        <div class="options-wrapper">
            <router-link to = "/" class = "nav-part home">HOME</router-link>
            <router-link to = "/buy" class = "nav-part buy">BUY</router-link>
            <router-link to = "/sell" class = "nav-part sell">SELL</router-link>
            <router-link to = "/wishlist" class = "nav-part wishlist">WISHLIST</router-link>
        </div>
        <div v-if = "this.$route.name === 'Buy'" style = "min-width: 18vw"></div>
    </div>
</template>

<script>
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import pageSidebar from './pageSidebar.vue';
import Filters from './Filters.vue';
export default{
    name: "pageNav",
    components: { Filters, Button, Dropdown, pageSidebar },
    data(){
        return{
            selectedVal: "",
            options: [ 'Price: Low to High', 'Price: High to Low', 'Newly Listed', 'Seller Rating' ],
        }
    },
}
</script>

<style scoped>
.wrapper{
    width: 100%;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
}

.filter-block{
    display: flex;
    gap: 1rem;
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


#filters{
    padding-left: 10px;
    padding-right: 5px;
}
</style>