<template>
    <div class="wrapper">
        <pageSidebar />
        <div class="options-wrapper">
            <Button @click = 'this.$router.push("/")' text class = "nav-part home">HOME</Button>
            <Button @click = 'this.$router.push("/buy")' text class = "nav-part buy">BUY</Button>
            <Button @click = 'this.$router.push("/sell")' text class = "nav-part sell">SELL</Button>
            <Button @click = 'this.$router.push("/wishlist")' text class = "nav-part wishlist">WISHLIST</Button>
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
    gap: 1rem;
    margin: 1rem;
}
.nav-part{
    letter-spacing: 0.2rem;
    margin-bottom: 0.1rem;
}
.nav-part:hover{
    margin-bottom: 0;
    border-bottom: 0.1rem solid white;
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