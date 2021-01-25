<script>
  export let text;
  export let iconName;
</script>

<style>
  .menu-button {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .menu-button-text {
    font-size: 7vh;
    line-height: 1;
    margin: 0;
    padding-right: 0.3em;
  }

  .menu-button-icon {
    height: 90%;
    width: auto;
  }
</style>

<div class="menu-button" on:click>
  <div>
    <h1 class="menu-button-text">{text}</h1>
  </div>
  <div>
    <!-- svelte-ignore a11y-missing-attribute -->
    <img class="menu-button-icon" src={`./images/${iconName}.svg`} />
  </div>
</div>
