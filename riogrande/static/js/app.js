(function() {

'use strict';

var $glossaries = $('.content-glossary');

$glossaries.on('click', '.glossary-header', function() {
  $(this).next('.glossary-info').toggleClass('glossary-hidden');
});

})();
