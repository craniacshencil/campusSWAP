<template>
    <div class="void">
        <pageHeader />
        <pageNav />
        <main>
            <h1>Sell your items, help a student</h1>
            <form>
                <FloatLabel>
                    <InputText id="Title of listing" v-model="title" class = "form-field" />
                    <label for="Title of listing">Title of listing</label>
                </FloatLabel>
                <FloatLabel>
                    <InputText id="Category" v-model="category" class = "form-field" />
                    <label for="Category">Category</label>
                </FloatLabel>
                <FloatLabel>
                    <InputText id="Price" v-model="price" class = "form-field" />
                    <label for="Price">Price</label>
                </FloatLabel>

                <FloatLabel>
                    <Textarea class = "desc" v-model="productDesc" autoResize rows="5" cols="30" />
                    <label for="Product Description">Product Description</label>
                </FloatLabel>
            </form>
        </main>
    </div>
</template>

<script>
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel'

export default{
    data(){
        return{
            style: "{width: 200px}",
            value: "",
        }
    },
    components:{ pageNav, pageHeader, InputText, FloatLabel }
}
</script>

<style scoped>
.void{
    background-color: #09090b;
    height: 100%;
    width: 100%;
    
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

h1{
    text-transform: uppercase; 
    font-weight: 300;
    letter-spacing: 0.4rem;
}

label{
    text-transform: uppercase;
    letter-spacing: 0.1rem;
}
.form-field{
    width: 500px;
    line-height: 30px;
}
.desc{
    background-color: #09090b;
    font-size: 16px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.desc:focus{
    border: 1px solid teal;
    outline: 1px solid teal;
}
</style>