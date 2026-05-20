<template>
  <button class="exit-course-button" @click="exitToCourse">
    Curso
  </button>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from 'vue'

function getExitUrl() {
  if (window.location.hostname === 'localhost' && window.location.port === '3030') {
    return 'http://localhost:3000/mi-primer-nodo-iot-ambiental/slides/'
  }
  return '../slides/'
}

function exitToCourse() {
  window.top.location.href = getExitUrl()
}

function handleKeydown(event) {
  if (event.key === 'Escape') {
    exitToCourse()
  }
}

onMounted(() => window.addEventListener('keydown', handleKeydown))
onBeforeUnmount(() => window.removeEventListener('keydown', handleKeydown))
</script>

<style>
.exit-course-button {
  position: fixed;
  top: 14px;
  right: 16px;
  z-index: 9999;
  border: 1px solid rgba(23,24,28,0.16);
  border-radius: 999px;
  background: rgba(255,255,255,0.78);
  color: #17181c;
  padding: 0.36rem 0.68rem;
  font-size: 0.72rem;
  font-weight: 760;
  cursor: pointer;
  backdrop-filter: blur(10px);
}
.exit-course-button:hover {
  border-color: #008f7a;
  color: #008f7a;
}
@media print {
  .exit-course-button {
    display: none;
  }
}
</style>
