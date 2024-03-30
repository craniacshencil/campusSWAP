<template>
<div class="void flex flex-column align-items-center">
    <pageHeader />
    <div class="listings-wrapper flex flex-wrap justify-content-evenly w-full align-items-center mt-8">
        <itemCard v-for="listing in listings" :key="listing.id" :product="listing" main_action = "Check for Approval" />
    </div>
</div>
</template>
<script> 
import pageHeader from '@/custom_comps/pageHeader.vue'
import itemCard from '@/custom_comps/itemCard.vue'
import axios from 'axios'
export default{
    data(){
        return{
           listings: null, 
        }
    },
    components: { pageHeader, itemCard },
    created(){
        axios.get("http://localhost:8000/admin_actions/get_unapproved_listings_and_resources")
        .then(response => {
            this.listings = response.data.unapproved_listings
        })
        .catch(error => console.log(error))
    }
}
</script>