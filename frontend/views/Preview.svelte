<script>
  import { onMount } from "svelte";
  import { _ } from "svelte-i18n";

  import { AppState } from "../defines";
  import { getLastPhoto, setState } from "../actions";

  import BottomMenu from "../components/BottomMenu.svelte";
  import MenuButton from "../components/MenuButton.svelte";
  import PrintButton from "../components/PrintButton.svelte";

  let lastFileName = "";

  function showIntro() {
    setState(AppState.INTRO);
  }

  onMount(async () => {
    lastFileName = await getLastPhoto();
  });
</script>

<style>
  .preview {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: stretch;
  }

  .photo-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    width: 100%;
    height: 80vh;
  }

  .photo-container img {
    padding-left: 5vh;
    padding-right: 5vh;
    padding-top: 5vh;
    padding-bottom: 5vh;
    object-fit: scale-down;
  }
</style>

<div class="preview">
  <div class="spacer" />
  {#if lastFileName}
    <div class="photo-container">
      <!-- svelte-ignore a11y-missing-attribute -->
      <img src={`./photos/${lastFileName}`} />
    </div>
  {/if}
  <BottomMenu>
    <MenuButton text={$_('back')} iconName="back" on:click={showIntro} />
    {#if lastFileName}
      <PrintButton
        filename={lastFileName}
        on:success={showIntro}
        on:cancel={showIntro} />
    {/if}
  </BottomMenu>
</div>
