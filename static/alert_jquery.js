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
}

var btns = document.getElementsByClassName('del-tombol');
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function (e) {
        const ket = this.getAttribute('data-ket');
        const href = this.getAttribute('data-href') ? this.getAttribute('data-href') : this.getAttribute('href');
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
                    this.parentElement.submit();
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
    })
}


const iconFlash = document.getElementById('flash').getAttribute('data-icon');
const titleFlash = document.getElementById('flash').getAttribute('data-title');
const textFlash = document.getElementById('flash').getAttribute('data-text');
const urlFlash = document.getElementById('flash').getAttribute('data-url');


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