<template>
    <div class="void">
        <pageHeader ref = "page_header" @getSearchTerm = "storeSearchTerm" />
        <!-- when on buy page -->
        <pageNav />
        <div class = "buy-header flex justify-content-between">
            <Filters class = "filter-btn" @getFiltersVal = "storeFilters" />
            <h2 class="custom-heading" >FIND THE GEAR YOU NEED</h2>
            <div style = "width: 9vw;"></div>
        </div>
        <div class = "search-summary" v-if = "searchTerm !== ''">Showing results for "{{ searchTerm }}"</div>
        <main class="item-card-container">
            <itemCard v-for="listing in listings" :key="listing.id" :product="listing" main_action = "Check Out" />
        </main>
        <div v-if="listings && listings.length === 0">No results found.</div>
    </div>
</template>

<script>
import itemCard from '@/custom_comps/itemCard.vue'
import pageHeader from '@/custom_comps/pageHeader.vue'
import pageNav from '@/custom_comps/pageNav.vue'
import Filters from '@/custom_comps/Filters.vue'
import axios from 'axios'
export default {
    data(){
        return{
            searchTerm: '',
            filters: [],
            listings: null,
        }
    },
    components: { Filters, itemCard , pageHeader, pageNav },
    methods: {
        storeSearchTerm(searchTerm){
            this.searchTerm = searchTerm
            this.simpleSearch(this.searchTerm)
        },

        storeFilters(filters){
            this.filters = filters
            this.filters.push({'searchTerm' : this.searchTerm})
            this.filteredSearch(this.filters)
        },

        simpleSearch(searchTerm) {
            axios.get("http://localhost:8000/products/simple_search", {
                params: {
                    searchTerm: searchTerm
                }
            })
            .then(response => {
                if (response.data && response.data.filteredProducts) {
                    this.listings = response.data.filteredProducts;
                } else {
                    this.listings = []; // Handle case when no products are returned
                }
                console.log(this.listings);
            })
            .catch(error => console.log(error));
        },

        filteredSearch(filtersJSON){
            console.log(filtersJSON)    
            axios.post("http://localhost:8000/products/filtered_search", filtersJSON)
            .then(response => console.log(response))
            .catch(error => console.log(error))
        },
        fetchListings(){
            axios.get("http://localhost:8000/products/all_approved_listings")
            .then(response => {
                this.listings = response.data.allApprovedListings
            })
            .catch(error => console.log(error))
        }
    },
       
    // when coming to buy page from another page, bringing the search term to the buy page 
    mounted(){
        if (this.$route.params.searchTerm) {
            this.storeSearchTerm(this.$route.params.searchTerm)
        } else {
            this.fetchListings();
        }
    },
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

.search-summary{
    text-transform: uppercase;
    font-size: 1.2rem;
    letter-spacing: 0.1rem;
    align-self: flex-start;
    margin-left: 1rem;
}
</style>
