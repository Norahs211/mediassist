window.addEventListener('DOMContentLoaded', event => {
    const tables = document.querySelectorAll('.datatablesSimple');
    tables.forEach(table => {
        new simpleDatatables.DataTable(table);
    });
});
