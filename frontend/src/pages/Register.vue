<template>
    <div class = "void">
        <h1>Register</h1>
        <div class="register-form">
            <InputGroup>
                <InputGroupAddon>
                    <i class = "pi pi-user"></i>
                </InputGroupAddon>
                <InputText v-model = "moodleID" id = "MoodleID" placeholder = MoodleID autofocus />
            </InputGroup>

            <InputGroup>
                <InputGroupAddon>
                    <i class = "pi pi-at"></i>
                </InputGroupAddon>
                <InputText v-model = "email" type = email label = Email placeholder = Email />
            </InputGroup>

            <InputGroup>
                <InputText v-model = "firstName" label = "First Name" placeholder = "First Name" />
                <InputText v-model = "lastName" label = "Last Name" placeholder = "Last Name" />
            </InputGroup>
            <Password v-model = password  placeholder = "Password" inputStyle = "width: 500px" toggleMask />
            <Password v-model = confirmPassword  placeholder = "Confirm Password" inputStyle = "width: 500px" toggleMask :feedback = false />

            <!-- <passField label = "Password" placeholder = "Password" @valChanged = "password" /> -->
            <!-- <passField label = "Confirm Password" placeholder = "Confirm Password" @valChanged = "confirmPassword" /> -->
            <Button @click = "submitForm" label = "Submit" />
        </div>
    </div>
</template>

<script>
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button'
import passField from '../custom_comps/passField.vue'
import Password from 'primevue/password';

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
    data(){
        return{
            isPasswordVisible: false,
            isConfirmPasswordVisible: false,
            passText: "",
            confirmPassText: "",
        }
    },
    methods: {
        togglePassword(event, variable){
            variable = !variable
        },

        submitForm(){
            const formData = {
                moodleID: this.moodleID,
                email: this.email,
                firstName: this.firstName,
                lastName: this.lastName,
                password: this.password,
            };

            axios.post('/api/save_form_data/', formData)
                
            .then(response => {
                console.log("success registered user");
            }).catch(error => {
                console.log("error when registering");
            });
        },
    }
}
</script>

<style>
.void{
    background-color: #09090b;
    height: 100%;
    width: 100%;
    
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