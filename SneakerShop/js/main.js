function toggleBlocks(showClass, hideClass) {
  var showBlock = document.querySelector('.' + showClass);
  var hideBlock = document.querySelector('.' + hideClass);
  
  // Показываем блок, скрываем другой блок
  showBlock.style.display = 'flex'; // Изменим на flex, чтобы соблюсти стили
  hideBlock.style.display = 'none';
}
