<template>
    <div class="void">
        <pageHeader />
        <pageNav />
        <div class = "buy-header flex justify-content-between">
            <Filters class = "filter-btn" @getFiltersVal = "storeFilters" />
            <h2 class="custom-heading" >FIND THE GEAR YOU NEED</h2>
            <div style = "width: 9vw;"></div>
        </div>
        <main class="item-card-container">
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
            <itemCard />
        </main>
    </div>
</template>

<script>
import itemCard from '@/custom_comps/itemCard.vue'
import pageHeader from '@/custom_comps/pageHeader.vue'
import pageNav from '@/custom_comps/pageNav.vue'
import Filters from '@/custom_comps/Filters.vue'
export default {
    data(){
        return{
            searchTerm: [],
            filters: [],
            searchTermAndFilters: [],
        }
    },
    components: { Filters, itemCard , pageHeader, pageNav },
    methods: {
        storeFilters(filters){
            this.filters = filters
        }
    }
}
</script>

<style scoped>
.void {
    margin: 0;
    background-color: #09090b;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.item-card-container {
    display: flex;
    flex-wrap: wrap; 
    justify-content: space-around;
    align-items: flex-start;
    width: 100%;
    max-width: 1600px;
    padding: 30px;
}

.buy-header{
    width: 100%;
    border-top: 0.5px solid white;
}
.custom-heading {
    letter-spacing: 0.2rem;
}

.filter-btn{
    margin-left: 1rem;
}
</style>
