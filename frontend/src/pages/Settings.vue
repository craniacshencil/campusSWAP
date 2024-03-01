<template>
    <header>
        <h1>CampusSwap</h1>
        <div class="user-icons flex flex-row gap-4">
            <Avatar icon = "pi pi-shopping-cart" size = "large" />
            <Avatar icon = "pi pi-user" shape = "circle" size = "large" />
        </div>
    </header>
    <div style="margin-left: 300px;">
        <h2>Reset Password</h2>
        <FloatLabel style="margin-top: 30px;">
            <Password v-model="value" inputId="password" :feedback="false" />
            <label for="password">Current Password</label>
        </FloatLabel>
        <FloatLabel style="margin-top: 30px;">
            <Password v-model="value" inputId="password" />
            <label for="password">New Password</label>
        </FloatLabel>
        <FloatLabel style="margin-top: 30px;">
            <Password v-model="value" inputId="password" />
            <label for="password">Confirm New Password</label>
        </FloatLabel>

        <Button style="margin-top: 30px;" @click = "submitForm" label = "Submit" />
    </div>
</template>

<script>
import Button from 'primevue/button';
import Avatar from 'primevue/avatar';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';


export default{
    components: { Avatar, Button, Password, FloatLabel }
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