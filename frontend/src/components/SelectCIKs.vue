<template>
      <v-flex
        mt-5
        xs12
      >
        <h2 class="headline font-weight-bold mb-3">Select multiple Central Index Keys (CIKs) for Topic Modeling</h2>
        <v-select
                v-model="selectedCIKs"
                :items="CIKs"
                label="Ex: 1002388, 1001614, 1001258"
                solo
                multiple
                @change="$emit('updateCIKs', selectedCIKs)"
        />
      </v-flex>
</template>

<script>
    export default {
        name: 'SelectCIKs',
        data: () => ({
            CIKs: [],
            selectedCIKs: []
        }),
        mounted () {
            // get CIKs
              fetch(process.env.VUE_APP_API_URL + '/get_CIKs')
              .then(response => response.json())
              .then((data) => {
                this.CIKs = data
              })
        }
    };
</script>
