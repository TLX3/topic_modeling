<template>
      <v-flex
        mt-5
        xs12
      >
        <div style="display: flex; justify-content: space-evenly;">
          <div>
            <div class="headline font-weight-bold mb-3">Select Company (CIK) for Topic Modeling</div>
            <v-select
                    color="#273a56"
                    v-model="selectedCIKs"
                    :items="CIKs"
                    label="Ex: 1002388, 1001614, 1001258"
                    solo
                    multiple
                    @change="$emit('updateCIKs', selectedCIKs)"
            />
          </div>
          <div>
            <div class="headline font-weight-bold mb-3">Select number of topics</div>
            <v-select
                    color="#273a56"
                    v-model="num_topics"
                    :items="topic_choices"
                    label="Ex: 10"
                    solo
                    @change="$emit('updateNumTopics', num_topics)"
            />
          </div>
        </div>
      </v-flex>
</template>

<script>
    export default {
        name: 'SelectCIKs',
        data: () => ({
            CIKs: [],
            selectedCIKs: [],
            num_topics: 5,
            topic_choices: [3, 4, 5, 6, 7, 8, 9, 10]
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
