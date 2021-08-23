document.addEventListener('DOMContentLoaded', () => {

    // functionality for like button
    const likeButtons = document.querySelectorAll('.like-button');
    likeButtons.forEach(likeButton => {
        likeButton.addEventListener('click', () => {
            likeButtonClick(likeButton);
        });
    });
});

function likeButtonClick(likeButton) {
    // gets the id of the post that the button accompanies, based on the id assigned
    const postID = parseInt(likeButton.id.slice(12,));

    // Gets like badge
    const likeBadge = document.querySelector(`#like-badge-${postID}`);
    
    // update like button text and badge display number
    if (likeButton.textContent === 'Like') {
        likeButton.textContent = 'Unlike';
        likeBadge.textContent = parseInt(likeBadge.textContent) + 1
        // add put method with AJAX
    } else {
        likeButton.textContent = 'Like';
        likeBadge.textContent = parseInt(likeBadge.textContent) - 1
        // add put method with AJAX
    };
}