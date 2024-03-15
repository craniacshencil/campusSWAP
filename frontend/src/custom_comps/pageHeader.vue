<template>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
    <header>
        <Toast position = "bottom-right" group = "br"/>
        <ConfirmPopup></ConfirmPopup>
        <h1>CampusSwap</h1>
        <InputGroup class = "search-bar">
            <InputText placeholder = "Search" />
            <Button icon = "pi pi-search" />
        </InputGroup>
        <div v-if = "this.$route.name !== 'Home'" class="user-icons flex flex-row gap-4">
            <Button text raised outlined class = "logout-button" @click = "confirm1($event)" icon = "pi pi-power-off" />
            <Button text raised outlined class = "settings-button" @click = "this.$router.push({ name : 'Settings'})" icon = "pi pi-user" />
        </div>

        <div v-else class = "flex flex-row gap-2">
            <Button class = "register-btn nav-btn" @click = "this.$router.push({name: 'Register'})">Register</Button>
            <Button v-if = "!this.isLoggedIn" class = "nav-btn" @click = "this.$router.push({ name: 'Login'})">Login</Button>
            <Button v-else text raised outlined class = "logout-button" @click = "confirm1($event)" icon = "pi pi-power-off" />
        </div>
    </header>
</template>

<script>
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Avatar from 'primevue/avatar';
import Toast from 'primevue/toast';
import ConfirmPopup from 'primevue/confirmpopup';
import axios from 'axios'

export default{
    components: { Toast, ConfirmPopup, Avatar, InputText, Button, InputGroup },
    data(){
        return{
            isLoggedIn: false,
        }
    },
    methods: {
        confirm1(event) {
            const userObject = JSON.parse(sessionStorage.user)
            this.$confirm.require({
                target: event.currentTarget,
                message: `${userObject.user.first_name}, you want to logout?`,
                icon: 'pi pi-exclamation-triangle',
                rejectClass: 'p-button-outlined p-button-sm',
                acceptClass: 'p-button-sm',
                rejectLabel: 'No',
                acceptLabel: 'Yes',
                accept: () => {
                    this.$toast.add({ severity: 'info', summary: 'Confirmed', detail: 'Logging out...', group: 'br', life: 750 });
                    axios.post('http://localhost:8000/apis/logout', {
                    }).then(response => {
                        this.$store.commit('toggleIsAuthenticated', false)
                        this.$store.commit('assignUser', null)
                        setTimeout(() => {this.$router.push('login')}, 800)
                    }).catch(error => {
                        console.log(error);
                    });
                },
            });
        }
    },
    mounted(){
        const loggedInfo = JSON.parse(sessionStorage.isAuthenticated);
        this.isLoggedIn = loggedInfo.authState;
        console.log(this.isLoggedIn)
    }
}
</script>

<style scoped>
header{
    width: 100%;
    padding: 0 20px;
    border-bottom: 1px solid white;
    display: flex; 
    justify-content: space-around;
    align-items: center;
    gap: 5rem;
}
h1{
    font-family: 'Cormorant Garamond';
    font-size: 3rem;
    margin: 1rem 0;
    /* margin-top: 15px; */
}
.nav-btn{
    font-weight: 600;
}

.logout-button, 
.settings-button{
    font-size: 2rem;
    border-radius: 50%;
    height: 3rem;
    width: 3rem;
    border: 0.1rem solid #22d3ee;
    
}
.logout-button:hover{
    transform: scale(1.3);
    transition: 500ms;
    color: black;
    background-color: #22d3ee;
    cursor: pointer;
}
.settings-button:hover{
    transform: scale(1.3);
    transition: 500ms;
    color: black;
    background-color: #22d3ee;
    cursor: pointer;
}

.register-btn{
    margin-right: 0.5rem;
}
</style>