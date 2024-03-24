<template>
    <pageHeader />
    <h1>Welcome {{ first_name }}!</h1>
    <div class = "main-wrapper">
        <div class="products-wrapper">
            You have {{ unapprovedListings }} unapproved listings!
        </div>
    </div>
    <div class = "resources-wrapper">
            You have {{ upnapprovedResources }} unapproved listings!
    </div>
    <div class = "ban-user-wrapper">
        Ban Users
    </div>
</template>

<script>
import pageHeader from '@/custom_comps/pageHeader.vue'
import axios from 'axios';
export default{
    components: { pageHeader },
    data(){
        return{
            unapprovedListings: null,
            unapprovedResources: null,
            first_name: "",
        }
    },
    created(){
        this.first_name = JSON.parse(sessionStorage.user).user.first_name 
        axios.get("http://localhost:8000/admin_actions/get_unapproved_listings_and_resources")
        .then((response) => {
            console.log(response)
            this.unapprovedListings = response.data.listings
        })
        .catch( error => console.log(error))
    }
}
</script>

<style scoped>
</style>