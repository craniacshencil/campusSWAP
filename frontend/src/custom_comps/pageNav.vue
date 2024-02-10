<template>
    <div class="wrapper">
        <pageSidebar />
        <div class="options-wrapper">
            <Button @click = 'this.$router.push("/")' text class = "nav-part home">HOME</Button>
            <Button @click = 'this.$router.push("/buy")' text class = "nav-part buy">BUY</Button>
            <Button @click = 'this.$router.push("/sell")' text class = "nav-part sell">SELL</Button>
            <Button @click = 'this.$router.push("/wishlist")' text class = "nav-part wishlist">WISHLIST</Button>
        </div>
        <div class="card flex justify-content-center align-items-center">
            <Dropdown v-model="selectedVal" :options="cities" optionLabel="name" placeholder="Filters" class="w-full md:w-14rem" />
        </div>
    </div>
</template>

<script>
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import pageSidebar from './pageSidebar.vue';
export default{
    name: "pageNav",
    components: { Button, Dropdown, pageSidebar },
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
.nav-part:hover{
    border-bottom: 2px solid white;
}

pageSidebar{
    flex: 2;
}
</style>