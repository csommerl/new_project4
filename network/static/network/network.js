document.addEventListener('DOMContentLoaded', () => {

    // functionality for like button
    const likeButtons = document.querySelectorAll('.like-button');
    likeButtons.forEach(likeButton => {
        likeButton.addEventListener('click', () => {
            likeButtonClick(likeButton);
        });
    });

    // functionality for follow button; try-catch is used for pages without follow button
    try {
        const followButton = document.querySelector('.follow-button');
        followButton.addEventListener('click', () => {
            followButtonClick(followButton);
        });
    } catch (error) {
        console.error(error); ////// does this error have to be logged in the console? maybe it could just be hidden with no problem
    };

    // functionality for edit button
    const editButtons = document.querySelectorAll('.edit-button');
    editButtons.forEach(editButton => {
        editButton.addEventListener('click', () => {
            editButtonClick(editButton);
        });
    });

});


function editButtonClick(editButton) {
    // get post id, post content paragraph
    const postID = parseInt(editButton.id.slice(12,));
    const postContentPar = document.querySelector(`#post-content-${postID}`);
    const originalHTMLContent = postContentPar.innerHTML;
    const originalTextContent = postContentPar.textContent;
    
    //// hide editInfoPar, redisplay when cancel is selected
    document.getElementById(`edit-info-${postID}`).style.display = 'none';
    
    // change display to textarea
    postContentPar.innerHTML = 
        `
        <form id="edit-form-${postID}">
            <div class="fieldWrapper form-group">
                <textarea maxlength="280" rows="4" style="width: 48rem" class="form-control m-3 mx-auto" name="edit-content-${postID}">${originalTextContent}</textarea>
            </div>
            <div class="form-group m-3 mx-auto" style="width: 10rem;">
                <input class="btn btn-primary" type="submit" id="save-edit-${postID}" value="Save">
                <button class="btn btn-secondary" id="cancel-edit-${postID}">Cancel</button>
            </div>
        </form>
        `;
    
    // Cancel
    cancelEditButton = document.querySelector(`#cancel-edit-${postID}`);
    cancelEditButton.addEventListener('click', () => {
        postContentPar.innerHTML = originalHTMLContent;
        document.getElementById(`edit-info-${postID}`).style.display = 'block';
    });
    
    // Save
    editForm = document.querySelector(`#edit-form-${postID}`);
    editForm.addEventListener('submit', (event) => {
        // prevent default, get formData
        event.preventDefault();
        const formData = new FormData(event.target);
        editContent = formData.get(`edit-content-${postID}`);
        
        // replace content for display
        postContentPar.innerHTML = 
            `
            <p>${editContent}</p>
            `;
        
        // send to database with fetch
        fetch(`/edit-post/${postID}`, {
            method: 'PUT',
            body: JSON.stringify({
                content: editContent
            })
        })

        document.getElementById(`edit-info-${postID}`).style.display = 'block';
        
        ///// add new "last edited on..."

    });
}


function followButtonClick(followButton) {
    // gets id of profile to follow
    const profilename = followButton.id.slice(14,);
    const followerCount = document.querySelector(`#${profilename}-follower-count`)

    // what to do based on current status
    if (followButton.textContent === 'Follow') {
        
        // update button text
        followButton.textContent = 'Unfollow';
        followerCount.textContent = parseInt(followerCount.textContent) + 1;

        // update database
        fetch(`/follow/${profilename}`, {
            method: 'POST'
        });

        //// display error message?

    } else {

        // update button text
        followButton.textContent = 'Follow';
        followerCount.textContent = parseInt(followerCount.textContent) - 1;

        // update database
        fetch(`/unfollow/${profilename}`, {
            method: 'POST'
        });

        //// display error message?

    };
}


function likeButtonClick(likeButton) {
    // gets the id of the post that the button accompanies, based on the id assigned
    const postID = parseInt(likeButton.id.slice(12,));

    // Gets like badge
    const likeBadge = document.querySelector(`#like-badge-${postID}`);
    
    // what to do based on current status
    if (likeButton.textContent === 'Like') {
        
        // update like button text and badge display number
        likeButton.textContent = 'Unlike';
        likeBadge.textContent = parseInt(likeBadge.textContent) + 1;
        
        // update database
        fetch(`/like/${postID}`, {
            method: 'POST'
        });

        //// display error message?
        
    } else {
        
        likeButton.textContent = 'Like';
        likeBadge.textContent = parseInt(likeBadge.textContent) - 1;

        fetch(`/unlike/${postID}`, {
            method: 'POST'
        });
        
        //// display error message?

    };
}