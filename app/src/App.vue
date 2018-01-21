<template>
  <v-app>
    <div>
      <div class="text-xs-center">
        <v-btn color="primary" @click="alert = !alert">Toggle</v-btn>
      </div>
      <v-alert color="error" :value="alert">
        Whoops! An error occured!
      </v-alert>
    </div> 
  </v-app>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      alert: false
    }
  }
}
</script>