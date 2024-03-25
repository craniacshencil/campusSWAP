<template>
    <div class="void">
        <pageHeader />
        <pageNav />
        <h1>Sell your items, help a student</h1>
        <form @submit.prevent = "submitForm">
            <FloatLabel>
                <InputText id="Title of listing" v-model="title" class = "form-field" required/>
                <label for="Title of listing">Title of listing</label>
            </FloatLabel>

            <FloatLabel>
                <InputText id="Category" v-model="category" class = "form-field" required/>
                <label for="Category">Category</label>
            </FloatLabel>

            <FloatLabel>
                <InputText type = number id="Price" v-model="price" class = "form-field" required/>
                <label for="Price">Price</label>
            </FloatLabel>

            <FloatLabel>
                <MultiSelect :showToggleAll="false" id="year" v-model="selectedYear" display = "chip" :options = "engineeringYears" 
                class = "form-field" />
                <label for="year">Which year students need this item?</label>
            </FloatLabel>

            <FloatLabel>
                <MultiSelect :showToggleAll="false" id="Branch" v-model="selectedBranch" display = "chip" :options = "engineeringBranch" 
                class = "form-field" />
                <label for="Branch">Which branch students would need this item?</label>
            </FloatLabel>

            <FloatLabel>
                <MultiSelect :showToggleAll="false" id="ItemType" v-model="selectedItemType" display = "chip" :options = "itemType" 
                class = "form-field" />
                <label for="ItemType">Item type</label>
            </FloatLabel>

            <FloatLabel>
                <Dropdown id="Condition" v-model="selectedCondition" display = "chip" 
                :options = "condition" class = "form-field" required/>
                <label for="Condition">Condition of Item</label>
            </FloatLabel>

            <FloatLabel>
                <Textarea class = "desc" v-model="productDesc" required/>
                <label for="Product Description">Product Description</label>
            </FloatLabel>
            <div class = "image-uploader">
                <label for = "uploader" class = "uploader-label">Upload Images</label>
                <Toast />
            
                <FileUpload name="image" url = "http://localhost:8000/products/image_url_gen" @upload="onAdvancedUpload($event)" 
                :auto= "true" filelimit = 15 accept="image/*" :maxFileSize="32e7">
                    <template #empty>
                        <p>Drag and drop files to here to upload.</p>
                    </template>
                </FileUpload>
            </div>
            <Button rounded outlined label = "Preview Listing" class = "preview-listing-btn" @click = "validateForm" />
        </form>
    </div>
</template>

<script>
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import Textarea from 'primevue/textarea';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel'
import MultiSelect from 'primevue/multiselect';
import Dropdown from 'primevue/dropdown';
import Message from 'primevue/message';
import FileUpload from 'primevue/fileupload';
import Toast from 'primevue/toast';
import Button from 'primevue/button'
import axios from 'axios';

export default{
    data(){
        return{
            engineeringYears: ["F.E", "S.E", "T.E", "B.E"],
            engineeringBranch: ["CS", "AIML", "DS", "Civil", "Mech", "EXTC", "IT"],
            itemType: ["Textbooks", "Stationery", "Tools", "Gadgets", "Electrical Components" ],
            condition: ["Brand New", "Used-Good Condition", "Used-Fair Condition", "Needs Repair" ],
            title: "",
            category: "",
            price: null,
            selectedYear: [],
            selectedBranch: [],
            selectedItemType: [],
            selectedCondition: [],
            productDesc: "",
            image_urls: [],
        }
    },
    components:{ Dropdown, Button, pageNav, pageHeader, InputText, FloatLabel, MultiSelect, Message, FileUpload, Toast, Textarea },
    methods:{
        onAdvancedUpload(event) {
            this.image_urls.push(JSON.parse(event.xhr.responseText)['image_url'])
            this.$toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 })
        },

        validateForm(){
            let validFlag = 1
            let selectFields = [
                {'Year' : this.selectedYear},
                {'Branch': this.selectedBranch},
                {'Item Condition' : this.selectedCondition},
                {'Item Type' : this.selectedItemType},
                {'Images': this.image_urls},
            ] 
            let textFields = [
                {'Title': this.title},
                {'Category' : this.category},
                {'Price' : this.price},
                {'Product Description' : this.productDesc},
            ]
            

            for(let field of textFields){
                if(!(Object.values(field)[0])){
                    this.$toast.add({ severity: 'error', summary: 'Empty Field', detail: `${Object.keys(field)[0]} field is empty`, life: 3000 })
                    validFlag = 0 
                }
            }
            console.log(validFlag)

            for(let field of selectFields){
                if(Object.values(field)[0].length == 0){
                    this.$toast.add({ severity: 'error', summary: 'Empty Field', detail: `${Object.keys(field)[0]} field is empty`, life: 3000 })
                    validFlag = 0 
                }
            }
            if(validFlag)
                this.submitForm()
        },

        submitForm(){
            const sessionInfo = JSON.parse(sessionStorage.user)
            this.$router.push({ name: "Listing details", params: {
            product : JSON.stringify({
                moodleID:sessionInfo.user.moodleID,
                title:this.title,
                category:this.category,
                price:this.price,
                selectedYear: this.selectedYear,
                selectedBranch: this.selectedBranch,
                selectedItemType:this.selectedItemType,
                selectedCondition:this.selectedCondition,
                productDesc:this.productDesc,
                image_urls:this.image_urls,
                adminApproval: false,
            })
            }})
        },
    },
}
</script>

<style scoped>
.void{
    background-color: #09090b;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

h1{
    text-transform: uppercase; 
    text-align: center;
    font-weight: 300;
    letter-spacing: 0.4rem;
    margin-bottom: 2rem;
}

label{
    text-transform: uppercase;
    letter-spacing: 0.1rem;
}

form{
    display: flex;
    gap: 1.75rem;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.uploader-label{
    color: #AAA;
}
.form-field{
    width: 50vw;
    line-height: 2rem;
}

.image-uploader{
    margin-top: 1rem;
    width: 50vw;
    background: #09090b;
}
.desc{
    align-self: flex-start;
    background-color: #09090b;
    font-size: 16px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 10rem;
    min-width: 50vw;
}

.desc:focus{
    border: 1px solid teal;
    outline: 1px solid teal;
}

.preview-listing-btn{
    margin: 2rem;
    text-transform: uppercase;
    line-height: 1.5rem;
    font-size: 1.25rem;
    width: 50vh;
    padding: 1rem;
}

.preview-listing-btn:hover{
    background-color: #22d3ee;
    color: #09090b;
    transition: 200ms ease-in;
}
</style>