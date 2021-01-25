<script>
  import { AppState } from "../defines";
  import { setState } from "../actions";

  import BottomMenu from "../components/BottomMenu.svelte";
  import MenuButton from "../components/MenuButton.svelte";

  function capturePhoto() {
    setState(AppState.CAPTURE);
  }

  function showGallery() {
    setState(AppState.GALLERY);
  }
</script>

<style>
  .intro {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: stretch;
  }

  .take-photo {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .take-photo h1 {
    margin: 0;
    font-size: 13vh;
    line-height: 1;
  }

  .take-photo .capture-button {
    width: 100%;
    margin-left: auto;
    margin-right: auto;
  }

  .take-photo .capture-button img {
    height: 22vh;
    width: auto;
  }
  .spacer {
    height: 20vh;
  }
</style>

<div class="intro">
  <div class="spacer" />
  <div class="take-photo" on:click={capturePhoto}>
    <h1>Sprav si fotku</h1>
    <div class="capture-button">
      <!-- svelte-ignore a11y-img-redundant-alt -->
      <img src="./images/camera.svg" alt="Take a photo" />
    </div>
  </div>
  <div class="menu">
    <BottomMenu>
      <MenuButton text="Galéria" iconName="galery" on:click={showGallery} />
    </BottomMenu>
  </div>
</div>
