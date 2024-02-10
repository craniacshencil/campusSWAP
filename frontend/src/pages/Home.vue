<template>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
<div class = "back-overlay">
    <div class="top-row">
        <h1 class = branding>CampusSwap</h1>
        <div class = options>
            <Button @click = "gotoLogin" label = "Login" />
            <Button @click = "gotoRegister" label = "Register" />
        </div>
    </div>
</div>
</template>
<script>
    import Button from 'primevue/button'
    export default{
        components:{ Button },
        data(){
            return{

            }
        },

        methods: {
            gotoLogin(){
                this.$router.push("/login")
            },

            gotoRegister() {
                this.$router.push('/register')
            }
        }
    }
</script>

<style scoped>
    .back-overlay{
        background-color: #172554;
        border-radius: 10px;
        border: 20px solid #22d3ee;
        width: 100%;
        height: 100%;
    }

    .top-row{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 0 20px;
    }
    h1.branding{
        display: inline-block; 
        color: white;
        font-size: 78px;
        font-family: "Cormorant Garamond";
        padding: 0;
        margin: 0;
    }

    Button{
        margin: 3px;
    }
</style>
