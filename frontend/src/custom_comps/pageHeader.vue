<template>
    <header>
        <Toast position = "bottom-right" group = "br"/>
        <ConfirmPopup></ConfirmPopup>
        <h1>CampusSwap</h1>
        <InputGroup class = "search-bar">
            <InputText placeholder = "Search" />
            <Button icon = "pi pi-search" />
        </InputGroup>
        <div class="user-icons flex flex-row gap-4">
            <Avatar class = "logout-button" @click = "confirm1($event)" icon = "pi pi-power-off" shape = "circle" size = "large" />
            <Avatar icon = "pi pi-user" shape = "circle" size = "large" />
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
    methods: {
        confirm1(event) {
            this.$confirm.require({
                target: event.currentTarget,
                message: `${this.$store.state.userStore.user.first_name}, you want to logout?`,
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
    margin-top: 15px;
}

.logout-button:hover{
    background-color: rgb(3, 224, 224);
    cursor: pointer;
}

.logout-button:active{
    background-color: #444;
}
</style>