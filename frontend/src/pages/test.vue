<template>
    <passField placeholder = "Password" label = "password" @valChanged = "collectVal" />
    <p>The value in the password field is: {{ finale }}</p>
</template>

<script>
    import passField from "../custom_comps/passField.vue"
    export default{
        components: { passField },
        data(){
            return{
                finale: "",
            }
        },
        methods: {
            collectVal(pass){
                console.log(pass)
                this.finale = pass
            },

        }
    }
</script>