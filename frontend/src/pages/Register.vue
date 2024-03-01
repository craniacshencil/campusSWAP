<template>
    <div class = "void">
        <h1>Register</h1>
        <form class="register-form">
            <InputGroup>
                <InputGroupAddon>
                    <i class = "pi pi-user"></i>
                </InputGroupAddon>
                <InputText v-model = "moodleID" type = "number" id = "MoodleID" placeholder = MoodleID autofocus required/>
            </InputGroup>

            <InputGroup>
                <InputGroupAddon>
                    <i class = "pi pi-at"></i>
                </InputGroupAddon>
                <InputText v-model = "email" type = email label = Email placeholder = Email required/>
            </InputGroup>

            <InputGroup>
                <InputText v-model = "firstName" label = "First Name" placeholder = "First Name" required />
                <InputText v-model = "lastName" label = "Last Name" placeholder = "Last Name" required/>
            </InputGroup>
            <Password v-model = password  placeholder = "Password" inputStyle = "width: 500px" toggleMask required />
            <Password v-model = confirmPassword  placeholder = "Confirm Password" inputStyle = "width: 500px" toggleMask :feedback = false required />

            <!-- <passField label = "Password" placeholder = "Password" @valChanged = "password" /> -->
            <!-- <passField label = "Confirm Password" placeholder = "Confirm Password" @valChanged = "confirmPassword" /> -->
            <Button @click = "submitForm" type = "submit" label = "Submit" />
        </form>
    </div>
</template>

<script>
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button'
import passField from '../custom_comps/passField.vue'
import Password from 'primevue/password';
import axios from 'axios'

export default{
    name: "Register",
    data(){
        return{
            password: "",
            confirmPassword: "", 
            moodleID : "",
            firstName : "",
            lastName: "",
            email: "",
        }
    },
    components: { InputGroup, InputGroupAddon, InputText, Button, passField, Password },
    methods: {
        submitForm(){
            const formData = {
                moodleID: this.moodleID,
                email: this.email,
                firstName: this.firstName,
                lastName: this.lastName,
                password: this.password,
            };

            axios.post('http://127.0.0.1:8000/apis/register', formData)
            .then(response => {
                console.log("success registered user");
            }).catch(error => {
                console.log("error when registering");
            });
        },
    }
}
</script>

<style scoped>
.void{
    background-color: #09090b;
    height: 100vh;
    width: 100vw;
    
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.register-form{
    padding: 50px 10px;
    border: 0.5px solid #ddd;
    border-radius: 10px;

    display: flex;
    flex-direction: column;
    gap: 1rem;
}
</style>