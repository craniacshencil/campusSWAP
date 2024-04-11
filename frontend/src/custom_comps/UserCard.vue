<template>
    <div class="card-wrapper surface-0 w-25rem border-round-md border-1 border-200 p-4 py-6">
        <Toast />
        <h1 class = "m-0 ml-2 mb-2">{{ this.firstName }} {{  this.lastName }}</h1>
        <h2 class = "m-0 ml-2 mb-4 text-300">{{ this.username }}</h2>
        <div class="user-fields text-xl">
            <div class = "user-field-section m-0 p-0 border-bottom-1 border-top-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-list mr-2 text-lg"></i>
                Listings
                <span class = "ml-auto">c1</span>
            </div>
            <div class = "user-field-section m-0 p-0 border-bottom-1 p-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-book mr-2 text-lg"></i>
                Resources
                <span class = "ml-auto">c1</span>
            </div>
            <div class = "user-field-section m-0 p-0 border-bottom-1 p-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-heart mr-2 text-lg"></i>
                Wishlist
                <span class = "ml-auto">c1</span>
            </div>
            <div class = "user-field-section m-0 p-0 border-bottom-1 p-1 p-3 pl-2 border-200
             flex justify-content-between align-items-center">
                <i class = "pi pi-star mr-2 text-lg"></i>
                Stars
                <span class = "ml-auto">c1</span>
            </div>
        </div>
        <Button @click = "banUser" class = "mt-3 w-full" severity = "danger" label = "BAN" raised />
    </div>
</template>

<script>
import Button from 'primevue/button'
import Toast from 'primevue/toast'
import axios from 'axios'
export default{
    props: {username: String, firstName: String, lastName: String},
    components: { Button, },
    methods: {
        banUser(){
            const moodleIDJSON = {
                moodleID: this.username
            }
            axios.post("http://localhost:8000/admin_actions/delete_user", moodleIDJSON)
            .then(response => {
                this.$toast.add({severity: "success", summary: "Deleted User Successfully!", life: 3000, })
                setTimeout(() => {this.$router.push({name : 'Ban User'})}, 1500)
            })
            .catch(error => console.log(error))
        },
    },
}
</script>

<style>
.user-field-section:hover{
    background: #22d3ee;
    color: black;
    cursor: pointer;
}
</style>