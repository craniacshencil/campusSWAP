<template>
    <div class="card-wrapper surface-0 w-25rem border-round-md border-1 border-200 p-4 py-6">
        <h1 class = "m-0 ml-2 mb-2">{{ firstName }} {{  lastName }}</h1>
        <h2 class = "m-0 ml-2 mb-4 text-300">{{ username }}</h2>
        <div class="user-fields text-xl">
            <div class = "user-field-section m-0 p-0 border-bottom-1 border-top-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-list mr-2 text-lg"></i>
                Listings
                <span class = "ml-auto">{{ listingsCount }}</span>
            </div>
            <div class = "user-field-section m-0 p-0 border-bottom-1 p-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-book mr-2 text-lg"></i>
                Resources
                <span class = "ml-auto">{{ resourcesCount }}</span>
            </div>
            <div class = "user-field-section m-0 p-0 border-bottom-1 p-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-heart mr-2 text-lg"></i>
                Wishlist
                <span class = "ml-auto">{{ wishlistCount }}</span>
            </div>
            <div class = "user-field-section m-0 p-0 border-bottom-1 p-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-star mr-2 text-lg"></i>
                Stars
                <span class = "ml-auto">{{ starsCount }}</span>
            </div>
        </div>
        <Button @click = "banUser" class = "mt-3 w-full" severity = "danger" label = "BAN" raised />
    </div>
</template>

<script>
import Button from 'primevue/button'
import axios from 'axios'
export default{
    props: {username: String, firstName: String, lastName: String},
    data(){
        return{
            listingsCount: 0,
            resourcesCount: 0,
            wishlistCount: 0,
            starsCount: 0,
        }

    },
    components: { Button, },
    methods: {
        banUser(){
            const moodleIDJSON = {
                moodleID: this.username
            }
            axios.post("http://localhost:8000/admin_actions/delete_user", moodleIDJSON)
            .then(response => {
                this.$emit("userBanned")
            })
            .catch(error => console.log(error))
        },
    },
    created(){
        axios.get(`http://localhost:8000/admin_actions/get_user_info/${this.username}`)
        .then(response => {
            console.log(response)
            this.listingsCount = response.data.listings
            this.resourcesCount = response.data.resources
            this.wishlistCount = response.data.wishlist
            this.starsCount = response.data.stars
        })
        .catch(error => console.log(error))
    }
}
</script>

<style>
.user-field-section:hover{
    background: #22d3ee;
    color: black;
    cursor: pointer;
}
</style>