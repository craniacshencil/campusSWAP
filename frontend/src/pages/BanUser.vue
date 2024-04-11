<template>
    <Toast />
    <pageHeader />
    <h1 class = "hello text-center text-7xl font-light uppercase">Ban Users</h1>
    <div class="user-cards-wrapper flex justify-content-around align-items-start flex-wrap">
        <UserCard @userBanned = "banFeedback" class = "m-5" v-for = "user in allUsers" :username = "user.username" :firstName = "user.first_name" :lastName = "user.last_name" :key = "user" />
    </div>
</template>

<script>
import pageHeader from '@/custom_comps/pageHeader.vue'
import Toast from 'primevue/toast'
import UserCard from '@/custom_comps/UserCard.vue'
import axios from 'axios'
export default{
    data(){
        return{
            allUsers: null,
        }
    },
    components: {pageHeader, UserCard, Toast },
    created(){
       axios.get("http://localhost:8000/admin_actions/get_all_users")
       .then(response => {
            this.allUsers = response.data.all_users
    })
       .catch(error => console.log(error))
    },
    methods: {
        banFeedback(){
            this.$toast.add({severity: "success", summary: "Deleted User Successfully!", detail: "Refresh to see changes", life: 3000, })
        },
    },
}
</script>

<style scoped>

</style>