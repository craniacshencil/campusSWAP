# 0. General
- [ ] Toast for register and login page instead of messages `frontend` 

# 1. Login
- [ ] Add Toast telling user about why they were redirected to the login page (can be done suing route params see `searchBar` functionality implemented)`frontend`  `backend`
- [ ] Improve styling `frontend` `Tejashri`

# 2. Register
- [ ] Improve styling `frontend` `Tejashri`
- [ ] Take care of possible errors with the phone number
	- [ ] the phonenumber should not be already present in the db `backend` 
	- [ ] phonenumber should be 10 digits `backend`
- [ ] Make sure user first name and last name match `college_students` DB `backend` 

# 3.Buy
- [ ] Use `filterData` to perform query and show matching listings  `backend` `Prathamesh` 
- [ ] Display the matching listings `frontend`

# 4.Sell
- [ ] Instead of `category` use `courses that need` field that is more accurate
- [ ] Make sure images are lesser than 32Mb and throw error when they are not `frontend`
- [ ] The images are rendering very slowly put a skeleton there to make sure it takes enough time

# 5. Home
- [ ] Add proper logo on top `frontend`  `Tejashri`
- [ ] Search bar should redirect to buy page with relevant info `backend` `Prathamesh`
- [ ] Clicking on each category should redirect to specific search on the buy page `backend` `Prathamesh`
- [ ] Change contact seller to view products on the cards `frontend` `easychange`
# 6. Detailed Listing
- [ ] Galleria component:
	- [ ] Store thumbnails in database too `backend`
	- [ ] Use 4:3 ratio for cropping (vue-advanced-cropper) `frontend`
	- [ ] The buttons near the thumbnail are not working`dunno`
# 7. User Settings
- [ ] Replicate Kaggle, Github style design and use modal/popup/sidebar instead of a whole page `frontend` 
- [ ] Users should be able to change their password `backend` `easychange` `frontend`
- [ ] Users are allowed to upload a bio and image for their avatar `backend` `frontend`
- [ ] Users are allowed to delete their account `backend` `frontend`
- [ ] Users are allowed to see their own listings, create a modal/popup to show all the different steps involved `backend` `frontend`
- [ ] Users can also see their resources being verified by admin in a similar way

# 8. Admin 
- [ ] Ability to ban users `frontend` `backend`
- [ ] Every listing has to be moderated by admin before it is seen on the sit `frontend` `backend`
- [ ] Resources section will also be moderated by admin

# 9. Payment Integration
- [ ] Integrate UPI or whatever it is

# 10. Resources section
- [ ] Allow users to create resources catalogues for technologies they are familiar with 
- [ ] Display resources to other users
# 11. Recommendation Algo
Can't be using ML here data is too less
- [ ] Probably use history + per user hover over product information + click on product info to recommend products