<!DOCTYPE html>
{% load static %}
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>KGM | Homepage</title>
  <meta content="" name="description">
  <meta content="" name="keywords">
</head>

<body>

  <!-- ======= Hero Section ======= -->
  <section id="hero">
    <div class="hero-container">
      <a href="index.html" class="hero-logo" data-aos="zoom-in"><img src="{{ MEDIA_URL }}logo1.jpg" alt=""></a>
      <h1 data-aos="zoom-in">Welcome To Konark Gunners Repository</h1>
      <h2 data-aos="fade-up">Designed for database management at 316 Artillery Regiment</h2>
      <div class="button-container">
        <button><a data-aos="fade-up" data-aos-delay="200" href="/login/" class="btn-get-started scrollto">Login</a></button>
        <button><a data-aos="fade-up" data-aos-delay="200" href="/view-list/" class="btn-get-started scrollto">View List</a></button>
      </div>
    </div>
  </section><!-- End Hero -->

  <!-- Additional content here -->

  <!-- Vendor JS Files -->
  <script src="{% static 'vendor/aos/aos.js' %}"></script>
  <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
  <script src="{% static 'vendor/glightbox/js/glightbox.min.js' %}"></script>
  <script src="{% static 'vendor/isotope-layout/isotope.pkgd.min.js' %}"></script>
  <script src="{% static 'vendor/swiper/swiper-bundle.min.js' %}"></script>



</body>
</html>
