<script>
  import { _ } from "svelte-i18n";

  import { createEventDispatcher } from "svelte";

  import { printPhoto } from "../actions";
  import { PrinterStatus } from "../defines";

  import MenuButton from "./MenuButton.svelte";
  import Spinner from "./Spinner.svelte";

  export let filename = "";

  const dispatch = createEventDispatcher();

  let showModal = false;
  let printState = "sending";

  async function print() {
    showModal = true;
    let status;
    try {
      status = await printPhoto(filename);
    } catch (err) {
      status = PrinterStatus.ABORTED;
    }
    if (
      status == PrinterStatus.PROCESSING ||
      status == PrinterStatus.COMPLETED
    ) {
      showModal = false;
      dispatch("success");
    } else {
      printState = "error";
    }
  }

  function cancel() {
    showModal = false;
    printState = "sending";
    dispatch("cancel");
  }

  function tryAgain() {
    printState = "sending";
    print();
  }
</script>

<style>
  .print-backdrop {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
  }

  .print-modal {
    width: 60%;
    height: 70vh;
    background-image: url("../images/trees.png");
    border: 5px white solid;
    text-align: center;
    padding-top: 5vh;
    z-index: 11;
  }

  .print-modal h1 {
    font-size: 7vh;
  }

  .spiner-sizer {
    padding-top: 5vh;
    font-size: 5vh;
  }

  .error-icon {
    height: 30vh;
    width: auto;
  }

  .button-group {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-content: center;
    padding-top: 2.5vh;
    padding-left: 1vh;
    padding-right: 1vh;
  }

  .button {
    border: 10px solid black;
    border-radius: 5%;
    padding: 2vh;
    font-size: 6vh;
    width: 40%;
  }
</style>

<MenuButton text="Vytlačiť" iconName="printer" on:click={print} />
{#if showModal}
  <div class="print-backdrop">
    <div class="print-modal">
      {#if printState == 'sending'}
        <div class="sending-to-printer">
          <h1>{$_('sending_to_printer')}</h1>
          <div class="spiner-sizer">
            <Spinner />
          </div>
        </div>
      {:else if printState == 'error'}
        <div class="sending-to-printer">
          <h1>{$_('printing_error')}</h1>
          <div>
            <!-- svelte-ignore a11y-missing-attribute -->
            <img class="error-icon" src="./images/error.svg" />
          </div>
          <div class="button-group">
            <div class="button" on:click={cancel}>{$_('cancel')}</div>
            <div class="button" on:click={tryAgain}>{$_('try_again')}</div>
          </div>
        </div>
      {/if}
    </div>
  </div>
{/if}
