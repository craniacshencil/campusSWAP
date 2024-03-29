<template>
<div class="void">
    <pageHeader />
    <div class="admin-dash-wrapper flex flex-column align-items-center">
        <h1 class = "text-7xl text-center">Welcome <span class = "text-cyan-400">{{ first_name }}!</span></h1>
        <div class = "main-wrapper w-9 h-25rem flex justify-content-between gap-3">
            <div class="vertical-wrapper w-7 flex flex-column align-items-center justify-content-between gap-3">
                <div class="listings-wrapper w-full h-16rem text-6xl pl-5 pt-2 font-bold flex flex-column justify-content-between"
                @click = "this.$router.push({name: 'Approve Listing'})">
                    <span>You have <span class = "inner-number">{{ unapprovedListings }}</span> unapproved listings!</span>
                    <icon class = "pi pi-arrow-right text-4xl font-bold align-self-end pr-5 pb-5" />
                </div>
                <div class = "ban-user-wrapper w-full h-9rem text-6xl pl-5 pt-2 font-bold flex flex-column justify-content-between">
                    Ban Users
                    <icon class = "pi pi-arrow-right text-4xl font-bold align-self-end pr-5 pb-5" />
                </div>
            </div>
            <div class = "resources-wrapper w-5 text-6xl pl-5 pt-2 font-bold flex flex-column justify-content-between">
                <span>You have <span class = "inner-number">{{ unapprovedResources }}</span> unapproved resources!</span>
                <icon class = "pi pi-arrow-right text-4xl font-bold align-self-end pr-5 pb-5" />
            </div>
        </div>
    </div>
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
            this.unapprovedListings = response.data.listings_count
            this.unapprovedResources = response.data.resources_count
        })
        .catch( error => console.log(error))
    }
}
</script>

<style scoped>
.void{
    height: 100vh;
    width: 100vw;
}

.listings-wrapper,
.ban-user-wrapper,
.resources-wrapper{
    background-color: rgb(50, 50, 50)
}

.inner-number{
    color: rgba(255, 0, 0, .8)
}

.listings-wrapper:hover span span,
.resources-wrapper:hover span span{
    transition: all ease-in-out 300ms;
    color: black;
}

.listings-wrapper:hover icon,
.resources-wrapper:hover icon,
.ban-user-wrapper:hover icon{
    transition: all ease-in-out 300ms;
    transform: translateX(.8rem) scale(1.2);
    color: black;
    font-weight: 900;
}
.listings-wrapper{
    border-top-left-radius: 1.5rem;
}

.listings-wrapper:hover{
    transition: all ease-in-out 300ms;
    cursor: pointer;
    background: #22d3ee;
    color: black;
    -webkit-box-shadow: -20px -14px 52px -20px rgba(34,211,238,1);
    -moz-box-shadow: -20px -14px 52px -20px rgba(34,211,238,1);
    box-shadow: -20px -14px 52px -20px rgba(34,211,238,1);
}

.ban-user-wrapper{
    border-bottom-left-radius: 1.5rem;
}

.ban-user-wrapper:hover{
    transition: all ease-in-out 300ms;
    cursor: pointer;
    background: #22d3ee;
    color: black;
    -webkit-box-shadow: -17px 18px 47px -6px rgba(34,211,238,0.53);
    -moz-box-shadow: -17px 18px 47px -6px rgba(34,211,238,0.53);
    box-shadow: -17px 18px 47px -6px rgba(34,211,238,0.53);
}

.resources-wrapper:hover{
    transition: all ease-in-out 300ms;
    cursor: pointer;
    background: #22d3ee;
    color: black;
    -webkit-box-shadow: 16px -2px 53px -6px rgba(34,211,238,1);
    -moz-box-shadow: 16px -2px 53px -6px rgba(34,211,238,1);
    box-shadow: 16px -2px 53px -6px rgba(34,211,238,1);
}
.resources-wrapper{
    border-top-right-radius: 1.5rem;
    border-bottom-right-radius: 1.5rem;
}
</style>