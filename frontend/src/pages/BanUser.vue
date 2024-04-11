<template>
    <pageHeader />
    <h1 class = "hello text-center text-7xl font-light uppercase">Ban Users</h1>
    <div class="user-cards-wrapper flex justify-content-around align-items-start flex-wrap">
        <UserCard class = "m-5" v-for = "user in allUsers" :username = "user.username" :firstName = "user.first_name" :lastName = "user.last_name" :key = "user" />
    </div>
</template>

<script>
import pageHeader from '@/custom_comps/pageHeader.vue'
import UserCard from '@/custom_comps/UserCard.vue'
import axios from 'axios'
export default{
    data(){
        return{
            allUsers: null,
        }
    },
    components: {pageHeader, UserCard },
    created(){
       axios.get("http://localhost:8000/admin_actions/get_all_users")
       .then(response => {
            this.allUsers = response.data.all_users
            console.log(this.allUsers)
    })
       .catch(error => console.log(error))
    },
}
</script>

<style scoped>

</style>