<template>
    <div class="wrapper">
        <pageSidebar />
        <div class="options-wrapper">
            <router-link to = "/" class = "nav-part home">HOME</router-link>
            <router-link to = "/buy" class = "nav-part buy">BUY</router-link>
            <router-link to = "/sell" class = "nav-part sell">SELL</router-link>
            <router-link to = "/wishlist" class = "nav-part wishlist">WISHLIST</router-link>
        </div>
        <div class="filter-block card flex justify-content-center align-items-center">
            <Dropdown v-model="selectedVal" :options="cities" optionLabel="name" placeholder="Sort by" class="w-full md:w-14rem" showClear />
            <Filters />
        </div>
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
            cities: [
                { name: 'Price: Low to High'},
                { name: 'Price: High to Low'},
                { name: 'Newly Listed'},
                { name: 'Seller Rating'},
            ],
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
.options-wrapper{
    display: flex;
    justify-content: space-between;
    margin: 1rem;
    gap: 0.8rem;
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

.filter-block{
    display: flex;
    gap: 1rem;
}

#filters{
    padding-left: 10px;
    padding-right: 5px;
}
</style>