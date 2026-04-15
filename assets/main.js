
// Auto-detect city from URL, highlight voice section
document.addEventListener('DOMContentLoaded', function() {
  // Smooth open FAQ - close others
  document.querySelectorAll('details').forEach(d => {
    d.addEventListener('toggle', function() {
      if (this.open) {
        document.querySelectorAll('details').forEach(other => {
          if (other !== this) other.removeAttribute('open');
        });
      }
    });
  });
});
