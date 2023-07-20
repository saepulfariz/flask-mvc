const iconFlash = $('#flash').data('icon');
const titleFlash = $('#flash').data('title');
const textFlash = $('#flash').data('text');
const urlFlash = $('#flash').data('url');
const baseurl = $('#baseurl').val();


if (iconFlash && urlFlash) {
    Swal.fire({
        icon: iconFlash,
        title: titleFlash,
        text: textFlash,
        footer: '<a href>Alert Pake Link</a>'
    }).then((result) => {
        if (result.value) {
            window.location.href = urlFlash;
        }
    })
} else if (iconFlash) {
    Swal.fire({
        icon: iconFlash,
        title: titleFlash,
        text: textFlash
    })
}

// footer: '<a href>Alert Biasa?</a>'

function deleteTombol(e) {
    const ket = e.getAttribute('data-ket');
    const href = e.getAttribute('data-href') ? e.getAttribute('data-href') : e.getAttribute('href');
    Swal.fire({
        title: 'Are you sure?',
        text: ket,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.value) {
            if (href) {
                window.location.href = href;
            } else {
                e.parentElement.submit();
            }
            // Swal.fire(
            // 	'Deleted!',
            // 	'Your file has been deleted.',
            // 	'success'
            // ).then((result) => {
            // if (result.value) {
            // 		window.location.href = href;
            // 		}
            // 	})
        }
    })
    e.preventDefault();
}

$('.del-tombol').on('click', function (e) {
    const ket = $(this).data('ket');
    const href = $(this).data('href') ? $(this).data('href') : $(this).attr('href');
    Swal.fire({
        title: 'Are you sure?',
        text: ket,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.value) {
            if (href) {
                window.location.href = href;
            } else {
                $(this).parent().submit();
            }
            // Swal.fire(
            // 	'Deleted!',
            // 	'Your file has been deleted.',
            // 	'success'
            // ).then((result) => {
            // if (result.value) {
            // 	window.location.href = href;
            // 	}
            // })
        }
    })
    e.preventDefault();
});