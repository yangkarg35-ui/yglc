document.getElementById('enrollForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    
    alert(name + ' ခင်ဗျာ ကျောင်းအပ်လွှာ လက်ခံရရှိပါပြီ။ ငွေလွှဲအတည်ပြုချက်ကို စစ်ဆေးပြီး YGLC မှ အမြန်ဆုံး ဆက်သွယ်ပေးပါမည်။');
    this.reset();
});