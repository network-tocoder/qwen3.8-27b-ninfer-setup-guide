param([Parameter(Mandatory=$true)][string]$Path)
$d = Get-Content -Raw $Path | ConvertFrom-Json
$choice = $d.choices[0]
$message = $choice.message
$usage = $d.usage
$reasoning = $usage.completion_tokens_details.reasoning_tokens
[PSCustomObject]@{
    FinishReason = $choice.finish_reason
    PromptTokens = $usage.prompt_tokens
    CompletionTokens = $usage.completion_tokens
    ReasoningTokens = $reasoning
    VisibleCharacters = if ($null -eq $message.content) { 0 } else { $message.content.Length }
} | Format-List

