/**
 * DocPageActions Component - Premium UX Edition
 *
 * Primary action: Copy Markdown (for AI assistance and documentation)
 * Secondary actions: Download Markdown, Ask ChatGPT, Ask Claude, Share
 *
 * Features:
 * - Client-side HTML-to-Markdown via Turndown (no API calls, offline-ready)
 * - Smooth icon morphing animations
 * - Keyboard shortcuts (Ctrl/Cmd+Shift+C to copy)
 * - Tooltips with action descriptions
 * - Full accessibility (ARIA, keyboard nav, focus states)
 * - Responsive design (collapses on mobile)
 */

import React, { useEffect, useCallback } from 'react';
import { useDoc } from '@docusaurus/plugin-content-docs/client';
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { siClaude } from "simple-icons/icons";
import TurndownService from 'turndown';

// ============================================================================
// ICONS - Optimized for animations
// ============================================================================

const CopyIcon = ({ className = '' }: { className?: string }) => (
    <svg
        className={`doc-actions-icon ${className}`}
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
    >
        <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
    </svg>
);

const CheckIcon = ({ className = '' }: { className?: string }) => (
    <svg
        className={`doc-actions-icon doc-actions-icon--success ${className}`}
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2.5"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
    >
        <polyline points="20 6 9 17 4 12" />
    </svg>
);

const DownloadIcon = () => (
    <svg
        className="doc-actions-icon"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
    >
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
        <polyline points="7 10 12 15 17 10" />
        <line x1="12" y1="15" x2="12" y2="3" />
    </svg>
);

const ChatGPTIcon = () => (
    <svg
        className="doc-actions-icon"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="currentColor"
        aria-hidden="true"
    >
        <path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zM3.6 18.304a4.47 4.47 0 0 1-.535-3.014l.142.085 4.783 2.759a.771.771 0 0 0 .78 0l5.843-3.369v2.332a.08.08 0 0 1-.033.062L9.74 19.95a4.5 4.5 0 0 1-6.14-1.646zM2.34 7.896a4.485 4.485 0 0 1 2.366-1.973V11.6a.766.766 0 0 0 .388.676l5.815 3.355-2.02 1.168a.076.076 0 0 1-.071 0l-4.83-2.786A4.504 4.504 0 0 1 2.34 7.872zm16.597 3.855l-5.833-3.387L15.119 7.2a.076.076 0 0 1 .071 0l4.83 2.791a4.494 4.494 0 0 1-.676 8.105v-5.678a.79.79 0 0 0-.407-.667zm2.01-3.023l-.141-.085-4.774-2.782a.776.776 0 0 0-.785 0L9.409 9.23V6.897a.066.066 0 0 1 .028-.061l4.83-2.787a4.5 4.5 0 0 1 6.68 4.66zm-12.64 4.135l-2.02-1.164a.08.08 0 0 1-.038-.057V6.075a4.5 4.5 0 0 1 7.375-3.453l-.142.08L8.704 5.46a.795.795 0 0 0-.393.681zm1.097-2.365l2.602-1.5 2.607 1.5v2.999l-2.597 1.5-2.607-1.5z" />
    </svg>
);

const ClaudeIcon = () => (
    <svg
        className="doc-actions-icon"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="currentColor"
        aria-hidden="true"
    >
        <path d={siClaude.path} />
    </svg>
);

const ChevronDownIcon = () => (
    <svg
        className="doc-actions-icon doc-actions-chevron-icon"
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
    >
        <polyline points="6 9 12 15 18 9" />
    </svg>
);

const ShareIcon = () => (
    <svg
        className="doc-actions-icon"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
    >
        <circle cx="18" cy="5" r="3" />
        <circle cx="6" cy="12" r="3" />
        <circle cx="18" cy="19" r="3" />
        <line x1="8.59" y1="13.51" x2="15.42" y2="17.49" />
        <line x1="15.41" y1="6.51" x2="8.59" y2="10.49" />
    </svg>
);

const MarkdownIcon = () => (
    <svg
        className="doc-actions-icon"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden="true"
    >
        <path d="M14 3v4a1 1 0 0 0 1 1h4" />
        <path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2z" />
        <path d="M9 15l2-2 2 2" />
        <path d="M11 13v4" />
    </svg>
);

// ============================================================================
// TURNDOWN SERVICE - Markdown extraction
// ============================================================================

const turndownService = new TurndownService({
    headingStyle: 'atx',
    codeBlockStyle: 'fenced',
    bulletListMarker: '-',
    emDelimiter: '*',
    strongDelimiter: '**',
});

// Custom rule to preserve code blocks with language hints
turndownService.addRule('codeBlock', {
    filter: (node) => {
        return node.nodeName === 'PRE' && node.querySelector('code') !== null;
    },
    replacement: (content, node) => {
        const codeElement = (node as HTMLElement).querySelector('code');
        if (!codeElement) return content;

        const className = codeElement.className || '';
        const langMatch = className.match(/language-(\w+)/);
        const lang = langMatch ? langMatch[1] : '';
        const code = codeElement.textContent || '';
        return `\n\`\`\`${lang}\n${code}\n\`\`\`\n`;
    },
});

// ============================================================================
// TOOLTIP COMPONENT - Simple hover tooltip
// ============================================================================

interface TooltipProps {
    content: string;
    shortcut?: string;
    children: React.ReactNode;
    position?: 'top' | 'bottom';
}

const Tooltip = ({ content, shortcut, children, position = 'bottom' }: TooltipProps) => (
    <div className="doc-actions-tooltip-wrapper">
        {children}
        <div className={`doc-actions-tooltip doc-actions-tooltip--${position}`} role="tooltip">
            <span>{content}</span>
            {shortcut && <kbd className="doc-actions-shortcut">{shortcut}</kbd>}
        </div>
    </div>
);

// ============================================================================
// MAIN COMPONENT
// ============================================================================

export function DocPageActions() {
    const doc = useDoc();
    const [copied, setCopied] = React.useState(false);
    const [downloaded, setDownloaded] = React.useState(false);

    // Detect platform for keyboard shortcut display
    const isMac = typeof navigator !== 'undefined' && /Mac|iPod|iPhone|iPad/.test(navigator.userAgent);
    const modKey = isMac ? '⌘' : 'Ctrl';

    /**
     * Extract markdown from the rendered page content.
     * Uses Turndown to convert HTML to Markdown client-side.
     * No external API calls - works offline with zero rate limiting.
     */
    const extractMarkdown = useCallback((): string => {
        const article = document.querySelector('article');
        if (!article) {
            return `# ${doc.metadata.title}\n\n${window.location.href}`;
        }

        const clone = article.cloneNode(true) as HTMLElement;

        // Remove UI elements we don't want in the markdown
        const selectorsToRemove = [
            '.theme-doc-footer',
            '.pagination-nav',
            '.doc-content-header',
            '.floating-actions',
            '.theme-code-block-copied-btn',
            '.docSidebarContainer',
            '.tocCollapsible',
            'button',
            '.admonition-icon',
            '.hash-link',
        ];

        selectorsToRemove.forEach(selector => {
            clone.querySelectorAll(selector).forEach(el => el.remove());
        });

        const hasH1 = clone.querySelector('h1');
        let markdown = '';

        if (!hasH1 && doc.metadata.title) {
            markdown = `# ${doc.metadata.title}\n\n`;
        }

        markdown += turndownService.turndown(clone.innerHTML);
        markdown += `\n\n---\nSource: ${window.location.href}`;

        return markdown;
    }, [doc.metadata.title]);

    // Copy markdown to clipboard
    const handleCopyMarkdown = useCallback(async () => {
        try {
            const markdown = extractMarkdown();
            await navigator.clipboard.writeText(markdown);
            setCopied(true);
            setTimeout(() => setCopied(false), 2500);
        } catch (err) {
            console.error('Failed to copy:', err);
            // Fallback: copy the page URL
            try {
                await navigator.clipboard.writeText(window.location.href);
                setCopied(true);
                setTimeout(() => setCopied(false), 2500);
            } catch {
                // Silent fail - clipboard might not be available
            }
        }
    }, [extractMarkdown]);

    // Download markdown file
    const handleDownloadMarkdown = useCallback(() => {
        try {
            const markdown = extractMarkdown();
            const title = doc.metadata.title || doc.metadata.id.split('/').pop() || 'document';
            const filename = `${title.replace(/[^a-zA-Z0-9-_ ]/g, '')}.md`;

            const blob = new Blob([markdown], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            setDownloaded(true);
            setTimeout(() => setDownloaded(false), 2500);
        } catch (err) {
            console.error('Failed to download:', err);
        }
    }, [extractMarkdown, doc.metadata.title, doc.metadata.id]);

    // Open in ChatGPT
    const handleOpenInChatGPT = useCallback(() => {
        const prompt = `Read from ${window.location.href} so I can ask questions about it.`;
        const chatGptUrl = `https://chat.openai.com/?hints=search&q=${encodeURIComponent(prompt)}`;
        window.open(chatGptUrl, '_blank', 'noopener,noreferrer');
    }, []);

    // Open in Claude
    const handleOpenInClaude = useCallback(() => {
        const prompt = `Read from ${window.location.href} so I can ask questions about it.`;
        const claudeUrl = `https://claude.ai/new?q=${encodeURIComponent(prompt)}`;
        window.open(claudeUrl, '_blank', 'noopener,noreferrer');
    }, []);

    // Share functionality
    const handleShare = useCallback(async () => {
        if (navigator.share) {
            try {
                await navigator.share({
                    title: doc.metadata.title,
                    url: window.location.href,
                });
            } catch {
                // User cancelled or error - silent fail
            }
        } else {
            // Fallback: copy link
            try {
                await navigator.clipboard.writeText(window.location.href);
                setCopied(true);
                setTimeout(() => setCopied(false), 2500);
            } catch {
                // Silent fail
            }
        }
    }, [doc.metadata.title]);

    // Keyboard shortcut handler
    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            // Ctrl/Cmd + Shift + C to copy markdown
            if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'c') {
                e.preventDefault();
                handleCopyMarkdown();
            }
            // Ctrl/Cmd + Shift + D to download
            if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'd') {
                e.preventDefault();
                handleDownloadMarkdown();
            }
        };

        document.addEventListener('keydown', handleKeyDown);
        return () => document.removeEventListener('keydown', handleKeyDown);
    }, [handleCopyMarkdown, handleDownloadMarkdown]);

    return (
        <div className="doc-page-actions" role="toolbar" aria-label="Page actions">
            {/* Split Button: Main action + Dropdown trigger */}
            <div className={`doc-page-actions-split ${copied ? 'doc-page-actions-split--success' : ''}`}>
                {/* Primary Action: Copy Markdown */}
                <Tooltip
                    content={copied ? 'Copied!' : 'Copy as Markdown'}
                    shortcut={copied ? undefined : `${modKey}+⇧+C`}
                    position="bottom"
                >
                    <button
                        className={`doc-page-actions-main ${copied ? 'doc-page-actions-main--success' : ''}`}
                        onClick={handleCopyMarkdown}
                        aria-label={copied ? 'Copied to clipboard' : 'Copy page as Markdown'}
                        aria-pressed={copied}
                    >
                        <span className="doc-actions-icon-wrapper">
                            {copied ? <CheckIcon /> : <CopyIcon />}
                        </span>
                        <span className="doc-page-actions-label">
                            {copied ? 'Copied!' : 'Copy'}
                        </span>
                    </button>
                </Tooltip>

                {/* Dropdown trigger */}
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <button
                            className="doc-page-actions-chevron"
                            aria-label="More actions"
                            aria-haspopup="menu"
                        >
                            <ChevronDownIcon />
                        </button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end" className="doc-page-actions-content">
                        <DropdownMenuItem
                            onClick={handleDownloadMarkdown}
                            className={downloaded ? 'doc-actions-item--success' : ''}
                        >
                            {downloaded ? <CheckIcon /> : <DownloadIcon />}
                            <span>{downloaded ? 'Downloaded!' : 'Download Markdown'}</span>
                            <kbd className="doc-actions-menu-shortcut">{modKey}+⇧+D</kbd>
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem onClick={handleOpenInChatGPT}>
                            <ChatGPTIcon />
                            <span>Ask ChatGPT</span>
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={handleOpenInClaude}>
                            <ClaudeIcon />
                            <span>Ask Claude</span>
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem onClick={handleShare}>
                            <ShareIcon />
                            <span>Share</span>
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            </div>
        </div>
    );
}

export default DocPageActions;
