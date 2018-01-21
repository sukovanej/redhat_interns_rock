<template>
  <v-app>
    <div>
      <div class="text-xs-center">
        <v-btn color="primary" @click="setAlert()">Toggle</v-btn>
      </div>
      <v-alert color="error" :value="alert">
        Whoops! An error occured!
      </v-alert>
    </div> 
  </v-app>
</template>

<script>
import {db} from './firebase'

export default {
  name: 'Main',
  firebase () {
    return {
      alert: {
        source: db.ref('/')
      }
    }
  },
  methods: {
    setAlert () {
      this.alert = !this.alert
      this.$firebaseRefs.alert.set(this.alert)
    }
  }
}
</script>