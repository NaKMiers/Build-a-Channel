# Thumbnail Generation Prompts — Why Everyone Pretends To Be Busy

Status: `prompt only / image not generated` (no image-generation tool available this session)

Canonical packaging file: `../../03-packaging.md`

When generating, save outputs here as `variant-a-generated.png` ... `variant-e-generated.png`
(1280x720). After generating, check each output's WIT against the white round-headed glasses
style in `projects/why-cheap-products-keep-getting-worse/assets/thumbnails/`; reject off-model WIT.

Recommended A/B order: B -> C -> A -> D -> E. Recommended winner: Variant B.

Full prompts and negative prompts for all 5 variants live in `../../03-packaging.md`
under "Thumbnail Generation Prompts".

Shared WIT identity block (in every prompt):

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon figure with a thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, a simple white body, and a clean bold silhouette. WIT should match the character style from the five restored `Why Cheap Products Keep Getting Worse` thumbnails. Do not give WIT hair, a shirt and tie, shoes, or any extra clothing detail.
```
