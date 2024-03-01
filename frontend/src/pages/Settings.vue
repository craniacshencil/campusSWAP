<template>
    <header>
        <h1>CampusSwap</h1>
        <div class="user-icons flex flex-row gap-4">
            <Avatar icon = "pi pi-shopping-cart" size = "large" />
            <Avatar icon = "pi pi-user" shape = "circle" size = "large" />
        </div>
    </header>
</template>

<script>
import InputGroup from 'primevue/inputgroup';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Avatar from 'primevue/avatar';

export default{
    components: { Avatar, InputText, Button, InputGroup }
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
</style>