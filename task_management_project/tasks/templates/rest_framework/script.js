const cards = document.querySelectorAll('.card');
const dropzones = document.querySelectorAll('.dropzone');

cards.forEach((card) => {
  card.addEventListener('dragstart', dargStart);
  card.addEventListener('drag', drag);
  card.addEventListener('dragend', dragEnd);
});

function dargStart() {
  //console.log('card: start');
  dropzones.forEach((dropzone) => {
    dropzone.classList.add('hightlight');
  });

  this.classList.add('is-dragging');
}

function drag() {
  //console.log('card: is dragging');
}

function dragEnd() {
  //console.log('card: end');
  dropzones.forEach((dropzone) => {
    dropzone.classList.remove('hightlight');
  });
  this.classList.remove('is-dragging');
}

dropzones.forEach((dropzone) => {
  dropzone.addEventListener('dragenter', dragEnter);
  dropzone.addEventListener('dragover', dragOver);
  dropzone.addEventListener('dragleave', dragLeave);
  dropzone.addEventListener('dragdrop', dragDrop);
});

function dragEnter() {
  //console.log('dropzone: enter in zone');
}

function dragOver() {
  //console.log('dropzone: over');
  this.classList.add('over');

  // get dragging card
  const cardBeingDragged = document.querySelector('.is-dragging');

  this.appendChild(cardBeingDragged);
}

function dragLeave() {
  //console.log('dropzone: leave');
  this.classList.remove('over');
}

function dragDrop() {
  //console.log('dropzone: dropped');
  this.classList.remove('over');
}
