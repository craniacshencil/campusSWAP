<template>
    <Toast />
    <div class = "void">
        <h1>Register</h1>
        <form class="register-form">
            <div class = "form-field">
                <InputGroup>
                    <InputGroupAddon>
                        <i class = "pi pi-user"></i>
                    </InputGroupAddon>
                    <InputText v-model = "moodleID" type = "number" id = "MoodleID" placeholder = MoodleID autofocus required/>
                </InputGroup>
                <small v-if = "errorMessage == alreadyExistingAccount">{{ alreadyExistingAccount }}</small>
                <small v-if = "errorMessage == invalidMoodleID">{{ invalidMoodleID }}</small>
            </div>

            <div class = "form-field">
                <InputGroup>
                    <InputGroupAddon>
                        <i class = "pi pi-at"></i>
                    </InputGroupAddon>
                    <InputText v-model = "email" type = email label = Email placeholder = Email required/>
                </InputGroup>
                <small v-if = "errorMessage == emailMismatch">{{ emailMismatch }}</small>
            </div>

            <div class="form-field">
                <InputGroup>
                    <InputText v-model = "firstName" label = "First Name" placeholder = "First Name" required />
                    <InputText v-model = "lastName" label = "Last Name" placeholder = "Last Name" required/>
                </InputGroup>
            </div>
            
            <div class="form-field">
                <InputGroup>
                    <InputGroupAddon>
                        <i class = "pi pi-phone"></i>
                    </InputGroupAddon>
                    <InputText v-model = "phonenumber" type = "number" id = "phonenumber" placeholder = "phonenumber" required/>
                </InputGroup>
            </div>
            
            <div class="form-field">
                <Password ref = "passfield" v-model = password  placeholder = "Password" inputStyle = "width: 500px" toggleMask required />
                <small v-if = "errorMessage == passwordWeak">{{ passwordWeak }}</small>
                <small v-if = "errorMessage == passwordWeak"></small>
                <small v-if = "errorMessage == passwordWeak">a. It should be atleast 8 characters long</small>
                <small v-if = "errorMessage == passwordWeak">b. Should include a capital letter, special character and a number</small>
            </div>

            <div class="form-field">
                <Password v-model = confirmPassword  placeholder = "Confirm Password" inputStyle = "width: 500px" toggleMask :feedback = false required />
                <small v-if = "errorMessage == passwordMismatch">{{  passwordMismatch }}</small>
            </div>

            <Button label = "Submit" @click = "validateForm" />
        <!-- Adding type = submit breaks all the django form validation -->
        <!-- But when type = submit is not present then all the fields are note required -->
        </form>
        <div class = "successful-registration" v-if = "errorMessage == noError">
            <Message severity = "success">Registration successful</Message>
            <router-link class = "login-redirect" to = "login">Redirect to Login</router-link>
        </div>
    </div>
</template>

<script>
import Toast from 'primevue/toast';
import InputGroup from 'primevue/inputgroup';
import Message from 'primevue/message';
import InputGroupAddon from 'primevue/inputgroupaddon';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button'
import Password from 'primevue/password';
import axios from 'axios'

export default{
    name: "Register",
    data(){
        return{
            password: "",
            confirmPassword: "", 
            moodleID : "",
            phonenumber: "",
            firstName : "",
            lastName: "",
            email: "",
            passwordStrength: "",
            errorMessage: "", 
            passwordMismatch: "Password and Confirm Password don't match", 
            passwordWeak: "Password is not strong enough",
            emailMismatch: "Entered email for the MoodleID is incorrect",
            invalidMoodleID:  "Entered MoodleID is non-existent",
            alreadyExistingAccount:  "Account for this MoodleID already exists",
            noError: "No Error"
        }
    },
    components: { Toast, Message, InputGroup, InputGroupAddon, InputText, Button, Password },
    methods: {
        validateForm(){
            let isValidated = true 
            const fields = [ 
                {'moodleID':this.moodleID},
                {'email' : this.email},
                {'firstName' : this.firstName},
                {'lastName' : this.lastName},
                {'phonenumber': this.phonenumber},
                {'password' : this.password },
                {'confirmPassword' : this.confirmPassword},
            ]
            for(let field of fields){
                if(!Object.values(field)[0]){
                    this.$toast.add({ severity: 'error', summary: 'Empty Field', detail: `${Object.keys(field)[0]} field is empty`, life: 3000 })
                    isValidated = false
                }
            }

            if(isValidated)
                this.submitForm();
        },
        submitForm(){
            const formData = {
                moodleID: this.moodleID,
                email: this.email,
                firstName: this.firstName,
                lastName: this.lastName,
                password: this.password,
                confirmPassword: this.confirmPassword,
                passwordStrength: this.$refs.passfield.meter.strength,
                phonenumber: this.phonenumber,
            }

            axios.post('http://127.0.0.1:8000/apis/register', formData)
            .then(response => {
                this.errorMessage = response.data.register_error
                console.log(this.errorMessage)
            }).catch(error => {
                console.log("error when registering: ", error);
            });

        },
    },
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

small{
    display: block;
    color: rgba(255, 0, 0, 0.7);
    margin-top: 0.1rem;
}

.login-redirect{
    display: block;
    text-decoration: none;
    text-align: center;
    color: white;
}

.login-redirect:hover{
    background-color: white;
    color: black;
    padding-bottom: 0.2rem;
    font-size: 1.1rem;
    font-weight: 700;
    border-radius: 0.4rem; 
}

.login-redirect:active{
    color: white;
    background-color: #09090b;
    border: 0.1rem solid white;
}

</style>