<template>
    <div class="void">
        <pageHeader />
        <pageNav />
        <h1>{{ h1Title }}</h1>
        <form>
                <FloatLabel>
                    <InputText id="Title of listing" v-model="title" class = "form-field" @input = "sendValues" required/>
                    <label for="Title of listing">Title of listing</label>
                </FloatLabel>

                <FloatLabel>
                    <InputText id="Category" v-model="category" class = "form-field" @input = "sendValues" required/>
                    <label for="Category">Category</label>
                </FloatLabel>

                <FloatLabel>
                    <InputText type = number id="Price" v-model="price" class = "form-field" @input= "sendValues" required/>
                    <label for="Price">Price</label>
                </FloatLabel>

                <FloatLabel>
                    <MultiSelect :showToggleAll="false" id="year" v-model="selectedYear" display = "chip" @change= "sendValues" :options = "engineeringYears" 
                    class = "form-field" />
                    <label for="year">Which year students need this item?</label>
                </FloatLabel>

                <FloatLabel>
                    <MultiSelect :showToggleAll="false" id="Branch" v-model="selectedBranch" display = "chip" @change= "sendValues" :options = "engineeringBranch" 
                    class = "form-field" />
                    <label for="Branch">Which branch students would need this item?</label>
                </FloatLabel>

                <FloatLabel>
                    <MultiSelect :showToggleAll="false" id="ItemType" v-model="selectedItemType" display = "chip" @change= "sendValues" :options = "itemType" 
                    class = "form-field" />
                    <label for="ItemType">Item type</label>
                </FloatLabel>

                <FloatLabel>
                    <Dropdown id="Condition" v-model="selectedCondition" display = "chip"  @change= "sendValues"
                    :options = "condition" class = "form-field" required/>
                    <label for="Condition">Condition of Item</label>
                </FloatLabel>

                <FloatLabel>
                    <Textarea class = "desc" v-model="productDesc" @input = "sendValues" required/>
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
            <div v-if = "isEditingListing" class="image-deleter-wrapper" flex justify-content-start>
            <label for = "deleter">Delete Images</label>
                <p>You currently have {{this.image_urls.length}} images uploaded</p>
                <div class = "image-deleter-inner-wrapper flex justify-content-start gap-3">
                    <div class = "image-deleter-element flex flex-column" v-for = "image_url in image_urls">
                        <img alt="user header" :src="image_url" style="width: 150px; height: auto;" />
                        <Button label = "Delete" severity = "danger" raised @click = "deleteImage(image_url)" />
                    </div>
                </div>
            </div> 
            <Button rounded outlined label = "Preview Listing" class = "preview-listing-btn" @click = "validateForm" />
        </form>
    </div>
</template>

<script>
import pageNav from '@/custom_comps/pageNav.vue';
import pageHeader from '@/custom_comps/pageHeader.vue';
import FileUpload from 'primevue/fileupload';
import Toast from 'primevue/toast';
import Button from 'primevue/button'
import Textarea from 'primevue/textarea';
import InputText from 'primevue/inputtext';
import FloatLabel from 'primevue/floatlabel'
import MultiSelect from 'primevue/multiselect';
import Dropdown from 'primevue/dropdown';
import Message from 'primevue/message';

export default{
    data(){
        return{
            isEditingListing: false,
            engineeringYears: ["F.E", "S.E", "T.E", "B.E"],
            engineeringBranch: ["CS", "AIML", "DS", "Civil", "Mech", "EXTC", "IT"],
            itemType: ["Textbooks", "Stationery", "Tools", "Gadgets", "Electrical Components" ],
            condition: ["Brand New", "Used-Good Condition", "Used-Fair Condition", "Needs Repair" ],
            title: "",
            category: "",
            price: "",
            productDesc: "",
            selectedYear: [],
            selectedBranch: [],
            selectedItemType: [],
            selectedCondition: [],
            image_urls: [],
            h1Title: "Sell your items, help a student",
            existingProductId: null,
        }
    },
    components:{ Textarea, InputText, FloatLabel, MultiSelect, Dropdown, Message, Button, pageNav, pageHeader, FileUpload, Toast },
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
            if(this.existingProductId)
                this.updateListing()
            else{
                console.log("new listing")
                console.log(this.existingProductId)
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
                }),
                fromSell: true
                }})
            }
        },

        updateListing(){
            const sessionInfo = JSON.parse(sessionStorage.user)
            console.log("update listing")
            console.log(this.existingProductId)
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
                id: this.existingProductId,
            }),
            fromSell: true,
            id: this.existingProductId ,
            }})
        },

        //when in edit-listing mode
         deleteImage(image_url){
            const deleteIndex = this.image_urls.indexOf(image_url)
            this.image_urls.splice(deleteIndex, 1)
         },
    },
    created(){
        //When sell.vue is used to edit the listing
        if(this.$route.params.id)
            this.existingProductId = this.$route.params.id
        if(this.$route.params.filledValues){
            this.h1Title = "Edit Listing"
            const filledVal = JSON.parse(this.$route.params.filledValues)
            console.log(filledVal)
            this.title = filledVal.title
            this.category = filledVal.category
            this.price = filledVal.price
            this.productDesc= filledVal.productDesc
            this.selectedYear= filledVal.selectedYear
            this.selectedBranch= filledVal.selectedBranch
            this.selectedItemType= filledVal.selectedItemType 
            this.selectedCondition= filledVal.selectedCondition
            this.image_urls = filledVal.image_urls
            this.isEditingListing = true
        }
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

form{
    display: flex;
    gap: 1.75rem;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

label{
    text-transform: uppercase;
    letter-spacing: 0.1rem;
}

.uploader-label{
    color: #AAA;
}

.form-field{
    width: 50vw;
    line-height: 2rem;
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


.image-uploader,
.image-deleter-wrapper{
    margin-top: 1rem;
    width: 50vw;
    background: #09090b;
}

.image-deleter-element{
    width: 150px;
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